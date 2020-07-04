from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QVBoxLayout, QPushButton
import sys
from PyQt5 import QtGui, QtCore


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 600
        self.width = 1000
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:green")

        hbox = QVBoxLayout()

        button = QPushButton("Push Button")
        button.setStyleSheet("color:white")
        button.setStyleSheet("background-color:blue")

        frame = QFrame()

        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color:red")
        frame.setLineWidth(0.6)

        hbox.addWidget(button)
        hbox.addWidget(frame)

        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())