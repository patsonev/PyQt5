from PyQt5.QtWidgets import QPushButton, QApplication, QDialog, QVBoxLayout, QLabel, QStackedWidget
import sys
from PyQt5 import QtGui


class StackWidget(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.stacked()

        self.show()

    def stacked(self):

        vbox = QVBoxLayout()

        self.stacked_widget = QStackedWidget()

        vbox.addWidget(self.stacked_widget)

        for x in range(0, 8):
            label = QLabel("Stacked child" + str(x))
            label.setFont(QtGui.QFont("Sanserif", 15))
            label.setStyleSheet("color:red")

            self.stacked_widget.addWidget(label)

            self.button = QPushButton("Stack " + str(x))
            self.button.setStyleSheet("background-color:orange")

            self.button.page = x

            self.button.clicked.connect(self.btn_clicked)

            vbox.addWidget(self.button)

        self.setLayout(vbox)

    def btn_clicked(self):
        self.button = self.sender()
        self.stacked_widget.setCurrentIndex(self.button.page)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = StackWidget()
    sys.exit(myapp.exec())