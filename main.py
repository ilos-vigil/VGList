from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
import sys
import os
import vgui


class MyWindow(QtCore.QMetaObject):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('vgui.ui', self)
        self.show()


class UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        app = QtWidgets.QApplication([])
        window = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QPushButton('Top'))
        layout.addWidget(QtWidgets.QPushButton('Bottom'))
        window.setLayout(layout)
        window.show()
        app.exec_()

class DB():
    def __init__(self):
        self.connect()
        self.create_tables()

    def connect(self):
        try:
            self.conn = sqlite3.connect('vglist.db')
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

    def load_tables(self):
        try:
            game_table = "SELECT * FROM GAME"
            self.cursor.execute(game_table)
            rows = self.cursor.fetchall()

            return rows
        except sqlite3.Error as e:
            print(e)

if __name__ == "__main__":
    # SQLite
    DB = DB()
    # UI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = vgui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
