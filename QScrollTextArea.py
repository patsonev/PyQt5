from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFormLayout, QGroupBox, QLabel, QScrollArea, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QWidget):

    def __init__(self, val):
        super().__init__()

        self.title = "This is Title"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.val = val

        self.init_window()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        form_layout = QFormLayout()
        group_box = QGroupBox("This is group box")

        label_list = []
        button_list = []

        for i in range(self.val):
            label_list.append((QLabel(f"Label {i}")))
            button_list.append(QPushButton(f"Click me {i}"))
            form_layout.addRow(label_list[i], button_list[i])

        group_box.setLayout(form_layout)

        scroll = QScrollArea()
        scroll.setWidget(group_box)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(300)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

        self.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window(20)
    sys.exit(myapp.exec())