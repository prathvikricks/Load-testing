from flask import Flask, request, jsonify
from random import randint
from time import sleep

app = Flask(__name__)

# Dummy user data for authentication
USERS = {
    "test_user": "password123",
    "example_user": "example_pass"
}

# Routes from the original project
@app.route("/")
def index():
    return "OK"

@app.route("/about")
def about():
    return "It's about."

@app.route("/random")
def random():
    sleep(randint(0, 2))
    return "It's late."

# Login route
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if USERS.get(username) == password:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid credentials."}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
