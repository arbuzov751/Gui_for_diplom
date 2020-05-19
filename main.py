import sys
from PyQt5 import QtWidgets
import Authorization
import Authorization_expert
import Menu_expert
import Menu_leader
from Class_add_expert import Add_expert_window

class Authorization_window(QtWidgets.QMainWindow, Authorization.Ui_Authorization):
    check_exit = 0

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_expert.clicked.connect(self.open_authrization_expert)
        self.pushButton_expert.clicked.connect(self.close)
        self.pushButton_leader.clicked.connect(self.open_menu_leader)
        self.pushButton_leader.clicked.connect(self.close)
        self.pushButton_exit.clicked.connect(self.close)

    def open_menu_leader(self):
        self.check_exit = 1
        self.Menu_leader = Menu_leader_window()
        self.Menu_leader.show()


    def open_authrization_expert(self):
        self.check_exit = 1
        self.Authorization_expert = Authorization_expert_window()
        self.Authorization_expert.show()

    def closeEvent(self, e):
        if self.check_exit == 0:
            result = QtWidgets.QMessageBox.question(self, "Exit", "Really quit?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                e.accept()
            else:
                e.ignore()


class Authorization_expert_window(QtWidgets.QMainWindow, Authorization_expert.Ui_Authorization_expert):
    check_exit = 0

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_next.clicked.connect(self.open_menu_expert)
        self.pushButton_next.clicked.connect(self.close)
        self.pushButton_exit.clicked.connect(self.back_to_authorization)
        self.pushButton_exit.clicked.connect(self.close)

    def open_menu_expert(self):
        self.check_exit = 1
        self.Menu_expert = Menu_expert_window()
        self.Menu_expert.show()

    def back_to_authorization(self):
        self.check_exit = 1
        self.Authorization = Authorization_window()
        self.Authorization.show()

    def closeEvent(self, e):
        if self.check_exit == 0:
            result = QtWidgets.QMessageBox.question(self, "Exit", "Really quit?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                e.accept()
            else:
                e.ignore()


class Menu_expert_window(QtWidgets.QMainWindow, Menu_expert.Ui_Menu_expert):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Exit", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


class Menu_leader_window(QtWidgets.QMainWindow, Menu_leader.Ui_Leader_menu):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_add_expert.clicked.connect(self.open_add_expert)

    def open_add_expert(self):
        add_expert = Add_expert_window()
        add_expert.exec_()

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Exit", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


def main():
    Authorization_app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Authorization_window()  # Создаём объект класса Authorization_window
    window.show()  # Показываем окно
    sys.exit(Authorization_app.exec_())  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
