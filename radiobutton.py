from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, \
    QLabel
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.groupBox = QGroupBox("What is your favorite sport?")
        self.radiobtn1 = QRadioButton("Football")
        self.radiobtn2 = QRadioButton("Basketball")
        self.radiobtn3 = QRadioButton("Tennis")
        self.label = QLabel()

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radio_button()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.label)

        self.label.setFont(QtGui.QFont("Sanserif", 25))

        self.setLayout(vbox)
        self.show()

    def radio_button(self):
        self.groupBox.setFont(QtGui.QFont("Sanserif", 15))

        hboxlayout = QHBoxLayout()

        self.radiobtn1.setIcon(QtGui.QIcon(self.iconName))
        self.radiobtn1.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn1.setFont(QtGui.QFont("Sanserif", 20))
        self.radiobtn1.toggled.connect(self.on_radio_btn)
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2.setIcon(QtGui.QIcon(self.iconName))
        self.radiobtn2.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 20))
        self.radiobtn2.toggled.connect(self.on_radio_btn)
        hboxlayout.addWidget(self.radiobtn2)

        self.radiobtn3.setIcon(QtGui.QIcon(self.iconName))
        self.radiobtn3.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif", 20))
        self.radiobtn3.toggled.connect(self.on_radio_btn)
        hboxlayout.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hboxlayout)

    def on_radio_btn(self):
        radiobtn = self.sender()

        if radiobtn.isChecked():
            self.label.setText("You have selected " + radiobtn.text())


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())