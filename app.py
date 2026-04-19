from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data (instead of database)
tables = {"1": "Available", "2": "Occupied"}
orders = []

# Home route
@app.route('/')
def home():
    return "SROTMS Running Successfully"

# Table status (SRS: Table Management)
@app.route('/tables')
def get_tables():
    return jsonify(tables)

# Create order (SRS: Order Management)
@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    orders.append(data)
    return jsonify({"message": "Order created", "order": data})

# Billing (SRS: Billing Module)
@app.route('/bill/<int:amount>')
def bill(amount):
    gst = amount * 0.18
    total = amount + gst
    return jsonify({
        "amount": amount,
        "gst": gst,
        "total": total
    })

if __name__ == '__main__':
    app.run()