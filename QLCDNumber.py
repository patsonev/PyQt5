from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLCDNumber
import sys
from PyQt5 import QtGui
import random


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.lcd = QLCDNumber()
        self.vbox = QVBoxLayout()

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox.addWidget(self.lcd)

        self.lcd.setStyleSheet("background-color:orange")
        self.setStyleSheet("background-color:#212f3d")

        button = QPushButton("Generate random number")
        button.clicked.connect(self.generate)
        button.setStyleSheet("background-color:white")
        self.vbox.addWidget(button)

        self.setLayout(self.vbox)

        self.show()

    def generate(self):
        rand = random.randint(0, 100)
        self.lcd.display(rand)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())