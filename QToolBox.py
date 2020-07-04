from PyQt5.QtWidgets import QWidget, QApplication, QToolBox, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui


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

        self.setStyleSheet("background-color:orange")

        vbox = QVBoxLayout()

        toolbox = QToolBox()
        toolbox.setStyleSheet("background-color:grey")
        vbox.addWidget(toolbox)

        label = QLabel()
        toolbox.addItem(label, "Python")

        label1 = QLabel()
        toolbox.addItem(label1, "Java")

        label2 = QLabel()
        toolbox.addItem(label2, "C++")

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())