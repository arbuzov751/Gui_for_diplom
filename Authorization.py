# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Authorization.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(432, 130)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Authorization.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Authorization)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_leader = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_leader.setGeometry(QtCore.QRect(10, 30, 191, 41))
        self.pushButton_leader.setObjectName("pushButton_leader")
        self.pushButton_expert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_expert.setGeometry(QtCore.QRect(220, 30, 191, 41))
        self.pushButton_expert.setObjectName("pushButton_expert")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(310, 90, 91, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        Authorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Авторизация"))
        self.pushButton_leader.setText(_translate("Authorization", "Руководитель"))
        self.pushButton_expert.setText(_translate("Authorization", "Эксперт"))
        self.pushButton_exit.setText(_translate("Authorization", "Выход"))
