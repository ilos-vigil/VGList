# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vgui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(740, 170, 291, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkBox_insert = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_insert.setObjectName("checkBox_insert")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox_insert)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_dev = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dev.setObjectName("label_dev")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_dev)
        self.lineEdit_developer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_developer.setObjectName("lineEdit_developer")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_developer)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_pub = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_pub.setObjectName("label_pub")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_pub)
        self.lineEdit_publisher = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_publisher)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_date = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_date.setObjectName("label_date")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_date)
        self.lineEdit_release = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_release.setObjectName("lineEdit_release")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_release)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.label_rating = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_rating.setObjectName("label_rating")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_rating)
        self.spinBox_rating = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_rating.setMinimum(1)
        self.spinBox_rating.setMaximum(100)
        self.spinBox_rating.setProperty("value", 100)
        self.spinBox_rating.setObjectName("spinBox_rating")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spinBox_rating)
        self.pushButton_update = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_update.setObjectName("pushButton_update")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pushButton_update)
        self.Insert = QtWidgets.QLabel(self.formLayoutWidget)
        self.Insert.setObjectName("Insert")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Insert)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(740, 10, 291, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.lineEdit_search = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.verticalLayout_2.addWidget(self.lineEdit_search)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.comboBox_column = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_column.setObjectName("comboBox_column")
        self.verticalLayout_2.addWidget(self.comboBox_column)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.pushButton_search = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_2.addWidget(self.pushButton_search)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_insert.setText(_translate("MainWindow", "Yes"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_dev.setText(_translate("MainWindow", "Developer"))
        self.label_pub.setText(_translate("MainWindow", "Publisher"))
        self.label_date.setText(_translate("MainWindow", "Release Date"))
        self.label_rating.setText(_translate("MainWindow", "Rating"))
        self.pushButton_update.setText(_translate("MainWindow", "Insert"))
        self.Insert.setText(_translate("MainWindow", "Insert?"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))

