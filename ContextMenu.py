from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu
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

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def contextMenuEvent(self, event):
        contex_menu = QMenu(self)

        new_action = contex_menu.addAction("New")
        open_action = contex_menu.addAction("Open")
        quit_action = contex_menu.addAction("Quit")

        action = contex_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_action:
            self.close()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())