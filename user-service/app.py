from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "user-service healthy"})

@app.route("/users")
def get_users():
    return jsonify([
        {"id": 1, "name": "Om Kale"},
        {"id": 2, "name": "Jane Doe"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



# Triggering CI build
