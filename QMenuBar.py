from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenuBar
import sys
from PyQt5 import QtGui


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"

        self.init_window()
        self.create_menu()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def create_menu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        edit_menu = main_menu.addMenu("Edit")
        view_manu = main_menu.addMenu("View")
        help_menu = main_menu.addMenu("Help")

        copy_action = QAction(QtGui.QIcon(self.iconName), "Copy", self)
        copy_action.setShortcut("Ctrl+f")
        file_menu.addAction(copy_action)

        cut_action = QAction(QtGui.QIcon(self.iconName), "Cut", self)
        cut_action.setShortcut("Ctrl+z")
        file_menu.addAction(cut_action)

        save_action = QAction(QtGui.QIcon(self.iconName), "Save", self)
        save_action.setShortcut("Ctrl+e")
        file_menu.addAction(save_action)

        exit_action = QAction(QtGui.QIcon(self.iconName), "Exit", self)
        exit_action.setShortcut("Shift+x")
        edit_menu.addAction(exit_action)
        exit_action.triggered.connect(sys.exit)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())