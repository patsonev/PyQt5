from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.spin_box = QSpinBox()
        self.label = QLabel(self)

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vlay = QVBoxLayout()

        self.spin_box.valueChanged.connect(self.is_changed)
        vlay.addWidget(self.spin_box)

        self.label.setFont(QtGui.QFont("Sanserif", 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        vlay.addWidget(self.label)

        self.setLayout(vlay)

        self.show()

    def is_changed(self):
        size = self.spin_box.value()
        self.label.setText(str(size))


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())