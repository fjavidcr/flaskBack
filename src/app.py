from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "Hello World from flask"})

@app.route('/users', methods=['GET'])
def usersHandler():
    return jsonify({"response": "Hello World from flask"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888", debug=True)