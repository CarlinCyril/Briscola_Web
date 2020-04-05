DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS player;

CREATE TABLE game (
  id TEXT PRIMARY KEY,
  gameType TEXT NOT NULL,
  gameName TEXT NOT NULL,
  numPlayers INTEGER DEFAULT 0,
  maxNumPlayers INTEGER NOT NULL,
  gameStatus TEXT NOT NULL
);

CREATE TABLE player (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  game TEXT NOT NULL,
  team INTEGER NOT NULL,
  FOREIGN KEY (game) REFERENCES briscolaGame (id)
);

-- Insert test data

INSERT INTO game (id, gameType, gameName, numPlayers, maxNumPlayers, gameStatus) VALUES (
    "d20e7949-8b42-445c-bca6-4adc58459a9e",
    "briscola",
    "Maghi's Game",
    1,
    2,
    "pending"
);

INSERT INTO game (id, gameType, gameName, numPlayers, maxNumPlayers, gameStatus) VALUES (
    "d4ce5bf13-6bb2-4e89-b3a7-f0349e0f2b11",
    "briscola",
    "Cirillo's Game",
    4,
    4,
    "ongoing"
);