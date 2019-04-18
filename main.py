from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
import sys
import os
import vgui


def setUI(vgui, db):
    rows = db.load_tables()

    vgui.tableWidget.setColumnCount(5)
    vgui.tableWidget.setRowCount(1)
    rowIndex = 0
    for row in rows:
        vgui.tableWidget.insertRow(5)
        vgui.tableWidget.row
        print(row)
        for i in range(1, len(row)):
            print(i)
            print(row[i])
            # Add text to the row
            vgui.tableWidget.setItem(
                rowIndex, i-1, QtWidgets.QTableWidgetItem(str(row[i])))
    rowIndex += 1


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
    db = DB()
    # UI
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    vgui = vgui.Ui_MainWindow()
    vgui.setupUi(window)
    setUI(vgui, db)
    window.show()

    sys.exit(app.exec_())
