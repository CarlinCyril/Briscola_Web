# REST services

import functools

from flask import (
    Blueprint, g, request, jsonify
)

from briscolaWeb.db import get_db

bp = Blueprint('restServices', __name__)

@bp.route('/game', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':

        query = "SELECT id, gameType, gameName, numPlayers, maxNumplayers, gameStatus FROM game WHERE gameStatus != 'over' "

        db = get_db()
        #error = None
        results = db.execute(query).fetchall()
        data = []
        for row in results:
            data.append(list(row))

        return jsonify(data)
