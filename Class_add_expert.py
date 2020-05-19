from PyQt5 import QtWidgets
import Add_expert
import sys


class Add_expert_window(QtWidgets.QDialog, Add_expert.Ui_Add_expert):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_exit.clicked.connect(self.close)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Exit", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            self.close()
        else:
            e.ignore()
