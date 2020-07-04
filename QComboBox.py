from PyQt5.QtWidgets import QDialog, QApplication, QComboBox, QLabel, QVBoxLayout
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
        self.combo = QComboBox()

        self.init_window()

        self.show()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.combo.addItem("Python")
        self.combo.addItem("Java")
        self.combo.addItem("C++")
        self.combo.addItem("C#")

        self.combo.currentTextChanged.connect(self.change_label)

        vbox.addWidget(self.combo)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 30))

        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def change_label(self):
        com = self.combo.currentText()
        self.label.setText(com)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())