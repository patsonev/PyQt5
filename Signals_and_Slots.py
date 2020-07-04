from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
# from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "Learning PyQt5"
        self.left = 100
        self.top = 100
        self.width = 1100
        self.height = 700
        self.iconName = "plioky.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_button()

        self.show()

    def create_button(self):
        button = QPushButton("Close", self)
        # button.move(100, 100)
        button.setGeometry(QtCore.QRect(100, 100, 400, 50))
        button.setIcon(QtGui.QIcon(self.iconName))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("blqh blqh blqh")
        button.clicked.connect(self.click_me)

    def click_me(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
