from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

budget_items = []

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/app')
def app_redirect():
    return redirect(url_for('serve_index'))

@app.route('/api/budget', methods=['GET'])
def get_budget():
    return jsonify(budget_items)

@app.route('/api/budget', methods=['POST'])
def add_budget_item():
    data = request.get_json()
    item = {
        'id': len(budget_items) + 1,
        'name': data.get('name'),
        'amount': data.get('amount')
    }
    budget_items.append(item)
    return jsonify(item), 201

@app.route('/api/budget/<int:item_id>', methods=['DELETE'])
def delete_budget_item(item_id):
    global budget_items
    budget_items = [item for item in budget_items if item['id'] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
