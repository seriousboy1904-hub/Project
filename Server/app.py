from flask import Flask, request, jsonify

app = Flask(__name__)

# Buyurtmalar ro'yxati
orders = []

@app.route("/new_order", methods=["POST"])
def new_order():
    data = request.json
    orders.append(data)
    return jsonify({"status": "ok", "message": "Order received"}), 200

@app.route("/get_orders", methods=["GET"])
def get_orders():
    return jsonify(orders), 200

@app.route("/order_taken", methods=["POST"])
def order_taken():
    data = request.json
    order_id = data.get("id")
    for o in orders:
        if o.get("id") == order_id:
            orders.remove(o)
            return jsonify({"status": "ok"}), 200
    return jsonify({"status": "error", "message": "Order not found"}), 404

@app.route("/")
def index():
    return "Server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
