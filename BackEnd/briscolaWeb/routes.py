import functools

from flask import (
    Blueprint, g, request, jsonify, abort, json
)

from .dbModels import DbPlayer, DbGame

bp = Blueprint('restServices', __name__)

@bp.route('/api/game', methods=('GET', 'POST'))
def getAllGames():
    if request.method == 'GET':
        games = DbGame.query.all()
        return jsonify([game.serialize for game in games])