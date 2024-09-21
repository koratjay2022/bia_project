from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample JSON data
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# @app.route('/api/data', methods=['POST'])
# def add_data():
#     new_item = request.json  
#     data.append(new_item)  
#     return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
