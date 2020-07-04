from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QHBoxLayout, QLabel
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
        self.slider = QSlider()
        self.label = QLabel("0")

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:green")

        hbox = QHBoxLayout()

        hbox.addWidget(self.slider)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(120)
        self.slider.valueChanged.connect(self.changed_value)

        self.label.setFont(QtGui.QFont("Sanserif", 20))
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def changed_value(self):
        size = self.slider.value()
        self.label.setText(str(size))


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())