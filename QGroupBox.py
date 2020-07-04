from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtCore, QtGui


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "This is title"
        self.left = 200
        self.top = 100
        self.width = 1100
        self.height = 700
        self.iconName = "plioky.ico"

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        group_box = QGroupBox("Select your favorite food")
        group_box.setFont(QtGui.QFont("Sanserif", 30))

        hbox.addWidget(group_box)

        vbox = QVBoxLayout()

        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton("Orange")
        vbox.addWidget(rad3)

        group_box.setLayout(vbox)
        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
