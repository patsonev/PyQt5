from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QLabel
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
        self.line_edit = QLineEdit(self)
        self.label = QLabel(self)

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QVBoxLayout()

        hbox.addWidget(self.line_edit)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.line_edit.returnPressed.connect(self.on_pressed)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def on_pressed(self):
        self.label.setText(self.line_edit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
