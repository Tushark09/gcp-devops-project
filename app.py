from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a dictionary to store names and their corresponding messages
messages = {}

@app.route("/", methods=["GET"])
def hello():
    return "Hello, I love you Riya!"

@app.route("/messages", methods=["GET", "POST"])
def get_or_create_message():
    if request.method == "GET":
        # Return all messages as a JSON response
        return jsonify(messages)
    elif request.method == "POST":
        # Create a new message
        name = request.json.get("name")
        message = request.json.get("message")
        if not name or not message:
            return jsonify({"error": "Both 'name' and 'message' fields are required."}), 400
        messages[name] = message
        return jsonify({"success": f"Message for '{name}' created successfully."}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

