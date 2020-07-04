from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QDialog, QPushButton
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

        vbox = QVBoxLayout()

        button = QPushButton("Open second dialog")
        button.setFont(QtGui.QFont("Sanserif", 20))
        button.clicked.connect(self.open_second_dialog)

        vbox.addWidget(button)

        self.setLayout(vbox)

        self.show()

    def open_second_dialog(self):
        # mydialog = QDialog()
        # mydialog.setModal(True)
        # mydialog.exec()

        mydialog = QDialog(self)
        mydialog.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())