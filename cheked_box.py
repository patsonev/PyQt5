from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QCheckBox, \
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

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_check_box()

        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)
        self.setLayout(vbox)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 25))
        vbox.addWidget(self.label)

        self.show()

    def create_check_box(self):
        self.group_box = QGroupBox("What is your favorite programming language?")
        self.group_box.setFont(QtGui.QFont("Sanserif", 20))
        hboxlayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon(self.iconName))
        self.check1.setIconSize(QtCore.QSize(15, 15))
        self.check1.setFont(QtGui.QFont("Sanserif", 15))
        self.check1.toggled.connect(self.check_box_toggled)
        hboxlayout.addWidget(self.check1)

        self.check2 = QCheckBox("C++")
        self.check2.setIcon(QtGui.QIcon(self.iconName))
        self.check2.setIconSize(QtCore.QSize(15, 15))
        self.check2.setFont(QtGui.QFont("Sanserif", 15))
        self.check2.toggled.connect(self.check_box_toggled)
        # self.check2.setChecked(True)
        hboxlayout.addWidget(self.check2)

        self.check3 = QCheckBox("Fortran")
        self.check3.setIcon(QtGui.QIcon(self.iconName))
        self.check3.setIconSize(QtCore.QSize(15, 15))
        self.check3.setFont(QtGui.QFont("Sanserif", 15))
        self.check3.toggled.connect(self.check_box_toggled)
        self.check3.toggled()
        hboxlayout.addWidget(self.check3)

        self.group_box.setLayout(hboxlayout)

    def check_box_toggled(self):
        if self.check1.isChecked():
            self.label.setText("You have selected : " + self.check1.text())

        if self.check2.isChecked():
            self.label.setText("You have selected : " + self.check2.text())

        if self.check3.isChecked():
            self.label.setText("You have selected : " + self.check3.text())


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())
