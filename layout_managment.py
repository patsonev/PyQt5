from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
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
        self.groupBox = QGroupBox("What is you favorite sport ?")

        self.init_window()
        self.create_layout()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()
        hbox.addWidget(self.groupBox)
        self.setLayout(hbox)

        self.show()

    def create_layout(self):
        hboxlayout = QHBoxLayout()

        button1 = QPushButton("Football", self)
        button1.setIcon(QtGui.QIcon(self.iconName))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        button1.setToolTip("The name of the game football")
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Basketball", self)
        button2.setIcon(QtGui.QIcon(self.iconName))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        button3 = QPushButton("Tennis", self)
        button3.setIcon(QtGui.QIcon(self.iconName))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        hboxlayout.addWidget(button3)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
