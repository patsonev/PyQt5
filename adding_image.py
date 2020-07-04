from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 220
        self.iconName = "plioky.ico"

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label_image = QLabel(self)
        pixmap = QtGui.QPixmap("football.jpg")
        label_image.setPixmap(pixmap)

        vbox.addWidget(label_image)
        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
