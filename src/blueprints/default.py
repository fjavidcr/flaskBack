from flask import Flask, jsonify, Blueprint

default_bp = Blueprint('default', __name__)


@default_bp.route('/', methods=['GET'])
def home():
    return jsonify({"response": "Hello!"})


@default_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"response": "Hello!"})
