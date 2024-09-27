from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory storage for users and students
users = {}
students = []


@app.route('/')
def index():
    return render_template('index.html')


# Login API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('id')
    password = data.get('password')

    if user_id in users and users[user_id] == password:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid ID or password"}), 401


# Registration API
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user_id = data.get('id')
    password = data.get('password')

    if user_id in users:
        return jsonify({"message": "User already registered"}), 409

    users[user_id] = password
    return jsonify({"message": "Registration successful"}), 201


# Student registration API
@app.route('/api/students', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        data = request.json
        students.append(data)
        return jsonify({
            "student": data,
            "message": "Successfully registered for Pygenicarc!"
        }), 201
    return jsonify(students)


if __name__ == '__main__':
    app.run(debug=True)
