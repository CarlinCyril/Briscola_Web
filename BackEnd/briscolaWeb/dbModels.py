from . import db

class DbPlayer(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    username = db.Column(db.String(64), unique=False, nullable=False)
    game = db.Column(db.String(64), db.ForeignKey('game.id'), unique=False, nullable=False)
    team = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def serialize(self):
     return {
        'id': self.id,
        'username': self.username,
        'game': self.game,
        'team': self.team,
     }

class DbGame(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.String(64), primary_key=True, unique=True, nullable=False)
    gameName = db.Column(db.String(64), unique=False, nullable=False)
    gameType = db.Column(db.String(64), unique=False, nullable=False)
    numPlayers = db.Column(db.Integer, nullable=False, default=0)
    maxNumPlayers = db.Column(db.Integer, nullable=False)
    gameStatus = db.Column(db.String(64), unique=False, nullable=False)

    def __repr__(self):
        return '<Game {}>'.format(self.gameName)
    
    @property
    def serialize(self):
     return {
        'id': self.id,
        'gameName': self.gameName,
        'gameType': self.gameType,
        'numPlayers': self.numPlayers,
        'maxNumPlayers': self.maxNumPlayers,
        'gameStatus': self.gameStatus,
     }