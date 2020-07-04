from PyQt5.QtWidgets import QWidget, QApplication, QTimeEdit, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore


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

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.my_time()

        self.show()

    def my_time(self):
        vbox = QVBoxLayout()

        time = QtCore.QTime()
        time.setHMS(13, 15, 20)

        time_edit = QTimeEdit()
        time_edit.setFont(QtGui.QFont("Sanserif", 30))
        time_edit.setTime(time)

        vbox.addWidget(time_edit)
        self.setLayout(vbox)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())