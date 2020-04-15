import uuid
from sqlalchemy.exc import IntegrityError

from flask import (
    Blueprint, request, jsonify,
)

from .dbUtils import getAllGamesNotOver, createNewGame, getGameById, getGameByName, getGamesNameContains

bp = Blueprint('restServices', __name__)

@bp.route('/api/game', methods=['GET'])
def getGames():
    searchString = request.args.get('search')
    print(searchString)
    if (searchString):
        #Get all games whose name contains the search substring and the status is not OVER
        # If none are found, return empty list
        games = getGamesNameContains(searchString)
    else:
        #Get all games whose status is not OVER
        games = getAllGamesNotOver()
    return jsonify([game.serialize for game in games])

@bp.route('/api/game/<game_id>', methods=['GET'])
def getGameWithId(game_id:str):
    game = getGameById(game_id)
    if game:
        return jsonify(game.serialize)
    else:
        return makeJsonError(404, "Game does not exist")

@bp.route('/api/game', methods=['POST'])
def postGame():
    data = request.get_json()
    gameName = data.get('gameName', '')
    # Check if a game with this name already exists
    existingGame = getGameByName(gameName)
    if (existingGame):
        return makeJsonError(409,"A game with this name already exists.")
    gameType = data.get('gameType', '')
    maxNumPlayers = data.get('maxNumPlayers', '')
    gameStatus = data.get('gameStatus', '')
    id = uuid.uuid1().hex
    numPlayers = 1
    result = createNewGame(id, gameName, gameType, numPlayers, maxNumPlayers, gameStatus)
    return jsonify(result.serialize), 201

# Method to return JSON error
def makeJsonError(status_code, message):
    response = jsonify({
        'errorMessage': message
    })
    response.status_code = status_code
    return response