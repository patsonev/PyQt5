from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QGridLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "Learning PyQt5"
        self.left = 100
        self.top = 100
        self.width = 1100
        self.height = 700
        self.iconName = "plioky.ico"
        self.groupBox = QGroupBox("What is favorite programming language ?")

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_layout()
        vbox = QVBoxLayout(self.groupBox)
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()

    def create_layout(self):
        gridlayout = QGridLayout()

        button = QPushButton("Python", self)
        button.setIcon(QtGui.QIcon(self.iconName))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        gridlayout.addWidget(button, 0, 0)

        button1 = QPushButton("C++", self)
        button1.setIcon(QtGui.QIcon(self.iconName))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        gridlayout.addWidget(button1, 0, 1)

        button2 = QPushButton("Java", self)
        button2.setIcon(QtGui.QIcon(self.iconName))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        gridlayout.addWidget(button2, 1, 0)

        button3 = QPushButton("C#", self)
        button3.setIcon(QtGui.QIcon(self.iconName))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        gridlayout.addWidget(button3, 1, 1)

        self.groupBox.setLayout(gridlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())