# REST services

import functools

from flask import (
    Blueprint, g, request, jsonify, abort, json
)

from briscolaWeb.db import get_db

bp = Blueprint('restServices', __name__)

@bp.route('/game', methods=('GET', 'POST'))
def getAllGames():
    if request.method == 'GET':
        db = get_db()
        query = "SELECT id, gameType, gameName, numPlayers, maxNumplayers, gameStatus FROM game WHERE gameStatus != 'over' "

        results = db.execute(query).fetchall()

        data = []
        #for row in results:
        #    data.append(list(row))
        #return jsonify(data)

        return json.dumps( [dict(ix) for ix in results])  

@bp.route('/game/<game_id>', methods=['GET'])
def getGameById(game_id:str):
    db = get_db()
    query = "SELECT id, gameType, gameName, numPlayers, maxNumplayers, gameStatus FROM game WHERE id = ?"

    results = db.execute(query,(game_id,)).fetchone()
    if results:
        data = []
        return jsonify(list(results))
    else:
        abort(404, "Game not found.")
