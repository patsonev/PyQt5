from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QButtonGroup, QHBoxLayout, QLabel
import sys
from PyQt5 import QtGui, QtCore


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "This is title"
        self.left = 200
        self.top = 100
        self.width = 1100
        self.height = 700
        self.iconName = "plioky.ico"
        self.button_group = QButtonGroup()
        self.label = QLabel("Nothing was clicked")


        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.label.setFont(QtGui.QFont("Sanserif", 30))
        hbox.addWidget(self.label)

        self.button_group.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton("Python")
        button.setIcon(QtGui.QIcon(self.iconName))
        button.setIconSize(QtCore.QSize(50, 50))
        self.button_group.addButton(button, 1)
        hbox.addWidget(button)

        button = QPushButton("Java")
        self.button_group.addButton(button, 2)
        button.setIcon(QtGui.QIcon(self.iconName))
        button.setIconSize(QtCore.QSize(50, 50))
        hbox.addWidget(button)

        button = QPushButton("C++")
        self.button_group.addButton(button, 3)
        button.setIcon(QtGui.QIcon(self.iconName))
        button.setIconSize(QtCore.QSize(50, 50))
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.show()

    def on_button_clicked(self, id):
        for button in self.button_group.buttons():
            if button is self.button_group.button(id):
                self.label.setText(button.text() + " was clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())