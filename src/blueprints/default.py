from flask import Flask, jsonify, Blueprint

default_bp = Blueprint('default', __name__)


@default_bp.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "Hello from flask in docker"})
