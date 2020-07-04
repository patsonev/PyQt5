from PyQt5.QtWidgets import QDialog, QApplication, QCompleter, QLineEdit, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.line = QLineEdit()

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        names = ["Bulgaria", "France", "USA", "Russia", "Germany", "Japan"]
        completer = QCompleter(names)

        self.line.setCompleter(completer)

        vbox.addWidget(self.line)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())