from flask import Flask, jsonify, Blueprint, request
from src.dao.imdbApi import ImdbApi

imdbApi_bp = Blueprint('imdbapi', __name__)

imdbApi_dao = None


@imdbApi_bp.route('/search/movie/<string:title>', methods=['GET'])
def basic_search(title):
    global imdbApi_dao
    if not imdbApi_dao:
        imdbApi_dao = ImdbApi()

    responseData = []
    max = request.args.get('max')

    if max:
        print('max: {}'.format(max))
        responseData = imdbApi_dao.search_movie(title=title, max=max)
    else:
        print('max: default')
        responseData = imdbApi_dao.search_movie(title=title)

    return jsonify(responseData)
