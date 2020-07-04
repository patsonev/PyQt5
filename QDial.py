from PyQt5.QtWidgets import QWidget, QApplication, QDial, QLabel, QVBoxLayout
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
        self.dial = QDial()
        self.label = QLabel(self)


        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.label.setFont(QtGui.QFont("Sanserif", 50))
        self.dial.valueChanged.connect(self.dial_changed)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)

        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def dial_changed(self):
        size = self.dial.value()
        self.label.setText(str(size))


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())
