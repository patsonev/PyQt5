from PyQt5.QtWidgets import QWidget, QApplication, QSizeGrip, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class Window(QWidget):

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

        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vbox = QVBoxLayout()
        size = QSizeGrip(self)
        vbox.addWidget(size)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
