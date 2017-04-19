from flask import jsonify
from app.api import api


@api.route('/hello_world', methods=['GET'])
def hello_world():
    return "Hello World!!"