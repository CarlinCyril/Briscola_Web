from .dbModels import db, DbPlayer, DbGame

# Database queries

def getAllGamesNotOver():
    return DbGame.query.filter(DbGame.gameStatus != 'OVER').all()

def getGameById(id: str):
    return DbGame.query.filter(DbGame.id == id).first()

def getGameByName(name: str):
    return DbGame.query.filter(DbGame.gameName == name).first()

def getGamesNameContains(substring: str):
    #return DbGame.query.filter(DbGame.gameStatus != 'OVER', DbGame.gameName.contains(substring)).all()
    return DbGame.query.filter(DbGame.gameName.contains(substring)).all()

def createNewGame(id: str, gameName: str, gameType: str, numPlayers: int, maxNumPlayers: int, gameStatus: str):
    new_game= DbGame(id=id,
                    gameName=gameName,
                    gameType=gameType,
                    numPlayers=numPlayers,
                    maxNumPlayers=maxNumPlayers,
                    gameStatus = gameStatus)
    db.session.add(new_game)
    db.session.commit()
    return new_game