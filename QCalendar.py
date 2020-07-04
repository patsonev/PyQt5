from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QCalendarWidget, QLabel
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
        self.calendar_var = QCalendarWidget()
        self.label = QLabel()

        self.init_window()
        self.calendar()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def calendar(self):
        vbox = QVBoxLayout()

        self.calendar_var.setGridVisible(True)
        self.calendar_var.selectionChanged.connect(self.on_selection_changed)

        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setStyleSheet("color:blue")

        vbox.addWidget(self.calendar_var)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def on_selection_changed(self):
        ca = self.calendar_var.selectedDate()
        self.label.setText(str(ca))


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())