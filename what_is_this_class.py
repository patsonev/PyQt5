from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QLabel
import sys
from PyQt5 import QtGui


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "This is just title"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        label = QLabel("Focus and press SHIFT + F1")
        hbox.addWidget(label)

        button = QPushButton("Click me", self)
        # button.move(100, 100)
        button.setWhatsThis("this is a button")
        hbox.addWidget(button)

        self.setLayout(hbox)


        self.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())