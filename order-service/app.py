from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "order-service healthy"})

@app.route("/orders")
def get_orders():
    return jsonify([
        {"id": 101, "user_id": 1, "item": "Book"},
        {"id": 102, "user_id": 2, "item": "Headphones"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
