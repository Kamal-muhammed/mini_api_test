from flask import Flask, request
import json

server = Flask(__name__)
stock = []

@server.route('/stock', methods=['POST'])
def add_stock():
    product = json.loads(request.data)
    stock.append(product)
    return json.dumps(stock), 201