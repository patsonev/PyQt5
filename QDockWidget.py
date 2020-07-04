from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QListWidget
import sys
from PyQt5 import QtGui, QtCore


class DockDialog(QMainWindow):

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

        self.create_dock_widget()

        self.show()

    def create_dock_widget(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Close")

        self.dock = QDockWidget("Dockable", self)
        self.list_widget = QListWidget()

        list = ["Python", "C++", "Java", "C#"]

        self.list_widget.addItems(list)

        self.dock.setWidget(self.list_widget)

        self.setCentralWidget(QTextEdit())

        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = DockDialog()
    sys.exit(myapp.exec())

