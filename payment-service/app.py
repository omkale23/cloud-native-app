from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "payment-service healthy"})

@app.route("/payments")
def get_payments():
    return jsonify([
        {"id": 201, "user_id": 1, "amount": 499.99},
        {"id": 202, "user_id": 2, "amount": 149.00}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
