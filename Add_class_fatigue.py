# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_class_fatigue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Class_fatigue(object):
    def setupUi(self, Class_fatigue):
        Class_fatigue.setObjectName("Class_fatigue")
        Class_fatigue.resize(380, 152)
        Class_fatigue.setMinimumSize(QtCore.QSize(380, 152))
        Class_fatigue.setMaximumSize(QtCore.QSize(380, 152))
        self.label_description_class = QtWidgets.QLabel(Class_fatigue)
        self.label_description_class.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.label_description_class.setObjectName("label_description_class")
        self.textEdit_description_class = QtWidgets.QTextEdit(Class_fatigue)
        self.textEdit_description_class.setGeometry(QtCore.QRect(150, 40, 221, 61))
        self.textEdit_description_class.setObjectName("textEdit_description_class")
        self.label_name_class = QtWidgets.QLabel(Class_fatigue)
        self.label_name_class.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.label_name_class.setObjectName("label_name_class")
        self.lineEdit_name_class = QtWidgets.QLineEdit(Class_fatigue)
        self.lineEdit_name_class.setGeometry(QtCore.QRect(150, 10, 221, 20))
        self.lineEdit_name_class.setObjectName("lineEdit_name_class")
        self.pushButton_exit = QtWidgets.QPushButton(Class_fatigue)
        self.pushButton_exit.setGeometry(QtCore.QRect(274, 110, 101, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_add_class = QtWidgets.QPushButton(Class_fatigue)
        self.pushButton_add_class.setGeometry(QtCore.QRect(164, 110, 101, 31))
        self.pushButton_add_class.setObjectName("pushButton_add_class")

        self.retranslateUi(Class_fatigue)
        QtCore.QMetaObject.connectSlotsByName(Class_fatigue)

    def retranslateUi(self, Class_fatigue):
        _translate = QtCore.QCoreApplication.translate
        Class_fatigue.setWindowTitle(_translate("Class_fatigue", "Добавление класса состояния"))
        self.label_description_class.setText(_translate("Class_fatigue", "Опишите класс состояния:"))
        self.label_name_class.setText(_translate("Class_fatigue", "<html><head/><body><p>Введите название <br/>класса состояния:</p></body></html>"))
        self.pushButton_exit.setText(_translate("Class_fatigue", "Отмена"))
        self.pushButton_add_class.setText(_translate("Class_fatigue", "Применить"))

