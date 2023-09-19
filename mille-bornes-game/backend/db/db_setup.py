import sqlite3

# Connect to SQLite3 database (it will create 'mille_bornes.db' if it doesn't exist)
conn = sqlite3.connect('mille_bornes.db')
cursor = conn.cursor()

# Create the Game table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Game (
   game_id INTEGER PRIMARY KEY AUTOINCREMENT,
   start_time DATETIME NOT NULL,
   end_time DATETIME,
   status TEXT NOT NULL CHECK(status IN ("Ongoing", "Completed", "Abandoned")),
   winner_id INTEGER,
   FOREIGN KEY(winner_id) REFERENCES Player(player_id)
)
''')

# Create the Player table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Player (
   player_id INTEGER PRIMARY KEY AUTOINCREMENT,
   game_id INTEGER NOT NULL,
   name TEXT NOT NULL,
   distance_covered INTEGER DEFAULT 0,
   state TEXT,
   is_winner BOOLEAN DEFAULT FALSE,
   FOREIGN KEY(game_id) REFERENCES Game(game_id)
)
''')

# Create the Card table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Card (
   card_id INTEGER PRIMARY KEY AUTOINCREMENT,
   card_type TEXT NOT NULL CHECK(card_type IN ("Distance", "Hazard", "Safety", "Remedy")),
   card_name TEXT NOT NULL,
   card_value INTEGER
)
''')

# Create the PlayerHand table
cursor.execute('''
CREATE TABLE IF NOT EXISTS PlayerHand (
   player_id INTEGER NOT NULL,
   card_id INTEGER NOT NULL,
   in_play BOOLEAN DEFAULT FALSE,
   PRIMARY KEY(player_id, card_id),
   FOREIGN KEY(player_id) REFERENCES Player(player_id),
   FOREIGN KEY(card_id) REFERENCES Card(card_id)
)
''')

# Create the GameDeck table
cursor.execute('''
CREATE TABLE IF NOT EXISTS GameDeck (
   game_id INTEGER NOT NULL,
   card_id INTEGER NOT NULL,
   dealt BOOLEAN DEFAULT FALSE,
   PRIMARY KEY(game_id, card_id),
   FOREIGN KEY(game_id) REFERENCES Game(game_id),
   FOREIGN KEY(card_id) REFERENCES Card(card_id)
)
''')

# Commit and close the connection
conn.commit()
conn.close()