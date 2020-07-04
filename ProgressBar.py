from PyQt5.QtWidgets import QApplication, QProgressBar, QDialog, QVBoxLayout, QPushButton
import sys
from PyQt5 import QtGui, QtCore
import time


class MyThread(QtCore.QThread):

    change_value = QtCore.pyqtSignal(int)

    def run(self):
        count = 0
        while count <= 100:
            count += 1
            time.sleep(0.1)
            self.change_value.emit(count)
        sys.exit()


class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.progress_bar = QProgressBar()
        self.thread = MyThread()

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 3px; padding: 1px} "
                                        "QProgressBar:chunk {background:orange}")
        self.progress_bar.setOrientation(QtCore.Qt.Vertical)
        self.progress_bar.setTextVisible(False)
        vbox.addWidget(self.progress_bar)

        self.setStyleSheet("background-color:#0d1729")

        button = QPushButton("Start progress bar")
        button.setStyleSheet("background-color:white")
        button.clicked.connect(self.start_progress_bar)
        vbox.addWidget(button)

        self.setLayout(vbox)

        self.show()

    def start_progress_bar(self):
        self.thread.change_value.connect(self.set_progress_value)
        self.thread.run()

    def set_progress_value(self, value):
        self.progress_bar.setValue(value)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())