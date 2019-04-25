import sqlite3

class DB():
    def __init__(self):
        self.connect()
        self.create_tables()

    def connect(self):
        try:
            self.conn = sqlite3.connect('vgdb.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def create_tables(self):
        try:
            game_table = """
                            CREATE TABLE IF NOT EXISTS game (
                                ID INTEGER PRIMARY KEY,
                                NAME VARCHAR2(50) NOT NULL,
                                DEVELOPER VARCHAR2(30),
                                PUBLISHER VARCHAR2(30),
                                RELEASE_DATE DATE DEFAULT CURRENT_DATE,
                                RATING NUMBER(3)
                            )
                        """
            default_row = "INSERT OR IGNORE INTO game VALUES (1,'The Long dark', 'Hinterland Studio Inc.', 'Hinterland Studio Inc.', '2017-08-01' , 100)"

            with self.conn:
                self.cursor.execute(game_table)
                self.cursor.execute(default_row)
        except sqlite3.Error as e:
            print(e)

    def load_tables(self, query):
        try:
            game_table = query
            self.cursor.execute(game_table)
            rows = self.cursor.fetchall()

            return rows
        except sqlite3.Error as e:
            print(e)

    def add_row(self, query):
        try:
            with self.conn:
                self.cursor.execute(query)
        except sqlite3.Error as e:
            print(e)
