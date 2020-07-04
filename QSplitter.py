from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QHBoxLayout, QSplitter, QLineEdit
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


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

        hbox = QHBoxLayout()

        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)
        # left.setStyleSheet("background-color:violet")

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        # bottom.setStyleSheet("background-color:brown")

        line_edit = QLineEdit()
        line_edit.setStyleSheet("background-color:orange")

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.setStyleSheet("background-color:violet")
        splitter1.addWidget(left)
        splitter1.addWidget(line_edit)
        splitter1.setSizes([200, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.setStyleSheet("background-color:brown")
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())