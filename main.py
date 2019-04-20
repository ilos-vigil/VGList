from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
import sys
import os
import vgui


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


def configure_table():
    vgui.tableWidget.setColumnCount(6)
    vgui.tableWidget.hideColumn(0)
    vgui.tableWidget.setHorizontalHeaderLabels(
        ["ID", "Name", "Developer", "Publisher", "Release Date", "Rating"])
    vgui.tableWidget.setSortingEnabled(False)
    vgui.tableWidget.setEditTriggers(
        QtWidgets.QAbstractItemView.NoEditTriggers)
    load_table()


def load_table(query="SELECT * FROM GAME"):
    rows = db.load_tables(query)

    vgui.tableWidget.setRowCount(0)  # remove all item on table
    vgui.tableWidget.setRowCount(len(rows))
    rowIndex = 0
    for row in rows:
        vgui.tableWidget.row
        # print(row)
        for i in range(0, len(row)):
            # print(i)
            # print(row[i])
            # Add text to the row
            vgui.tableWidget.setItem(
                rowIndex, i, QtWidgets.QTableWidgetItem(str(row[i])))
        rowIndex += 1


def add_column():
    vgui.comboBox_column.addItem("Name")
    vgui.comboBox_column.addItem("Developer")
    vgui.comboBox_column.addItem("Publisher")


def search():
    keyword = vgui.lineEdit_search.text()
    category = vgui.comboBox_column.currentText()
    query = f"SELECT * FROM GAME WHERE {category} LIKE '%{keyword}%'"
    load_table(query)


def insert():
    insert = vgui.checkBox_insert.isChecked()
    id = vgui.lineEdit_ID.text()
    name = vgui.lineEdit_name.text()
    developer = vgui.lineEdit_developer.text()
    publisher = vgui.lineEdit_publisher.text()
    release_date = vgui.lineEdit_release.text()
    rating = vgui.spinBox_rating.value()

    if insert:
        query = f"INSERT OR IGNORE INTO game (NAME, DEVELOPER, PUBLISHER, RELEASE_DATE, RATING) VALUES ('{name}', '{developer}', '{publisher}', '{release_date}' , {rating})"
    else:
        query = f"UPDATE game SET NAME = '{name}', DEVELOPER = '{developer}', PUBLISHER = '{publisher}', RELEASE_DATE = '{release_date}', RATING = {rating} WHERE ID = {id}"

    db.add_row(query)
    load_table()


def update():
    vgui.checkBox_insert.setChecked(False)
    vgui.lineEdit_ID.setText(vgui.tableWidget.item(
        vgui.tableWidget.currentRow(), 0).text())
    vgui.lineEdit_name.setText(vgui.tableWidget.item(
        vgui.tableWidget.currentRow(), 1).text())
    vgui.lineEdit_developer.setText(vgui.tableWidget.item(
        vgui.tableWidget.currentRow(), 2).text())
    vgui.lineEdit_publisher.setText(vgui.tableWidget.item(
        vgui.tableWidget.currentRow(), 3).text())
    vgui.lineEdit_release.setText(vgui.tableWidget.item(
        vgui.tableWidget.currentRow(), 4).text())
    vgui.spinBox_rating.setValue(int(vgui.tableWidget.item(
        vgui.tableWidget.currentRow(), 5).text()))
    vgui.pushButton_update.setText("Update")


def change():
    if vgui.checkBox_insert.isChecked:
        vgui.lineEdit_ID.setText("")
        vgui.lineEdit_name.setText("")
        vgui.lineEdit_developer.setText("")
        vgui.lineEdit_publisher.setText("")
        vgui.lineEdit_release.setText("")
        vgui.spinBox_rating.setValue(100)
        vgui.pushButton_update.setText("Insert")


def setUI():
    configure_table()
    add_column()
    vgui.pushButton_search.clicked.connect(search)
    vgui.pushButton_update.clicked.connect(insert)
    vgui.checkBox_insert.stateChanged.connect(change)
    vgui.tableWidget.doubleClicked.connect(update)


if __name__ == "__main__":
    db = DB()
    # UI
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    vgui = vgui.Ui_MainWindow()
    vgui.setupUi(window)
    setUI()
    window.show()

    sys.exit(app.exec_())
