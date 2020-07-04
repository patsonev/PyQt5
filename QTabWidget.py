from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QWidget, QVBoxLayout, QDialogButtonBox, QLabel,\
    QLineEdit, QGroupBox, QComboBox, QCheckBox
import sys


class Tab(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Tab Widget")
        self.setWindowIcon(QtGui.QIcon("plioky.ico"))

        vbox = QVBoxLayout()
        tab_widget = QTabWidget()

        button_box = QDialogButtonBox(QDialogButtonBox().Ok | QDialogButtonBox().Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        tab_widget.addTab(TabContact(), "Contact Details")
        tab_widget.addTab(PersonDetails(), "Personal Details")

        vbox.addWidget(tab_widget)
        vbox.addWidget(button_box)

        self.setLayout(vbox)


class TabContact(QWidget):

    def __init__(self):
        super().__init__()

        name_label = QLabel("Name: ")
        name_edit = QLineEdit()

        phone_label = QLabel("Phone: ")
        phone_edit = QLineEdit()

        email_label = QLabel("Email: ")
        email_edit = QLineEdit()

        address_label = QLabel("Adress: ")
        address_edit = QLineEdit()

        vbox = QVBoxLayout()

        vbox.addWidget(name_label)
        vbox.addWidget(name_edit)

        vbox.addWidget(phone_label)
        vbox.addWidget(phone_edit)

        vbox.addWidget(email_label)
        vbox.addWidget(email_edit)

        vbox.addWidget(address_label)
        vbox.addWidget(address_edit)

        self.setLayout(vbox)


class PersonDetails(QWidget):

    def __init__(self):
        super().__init__()

        group_box = QGroupBox("Select your gender")
        group_box1 = QGroupBox("Select your favorite programming language")

        python = QCheckBox("Pyhton")
        cpp = QCheckBox("C++")
        java = QCheckBox("Java")
        csharp = QCheckBox("C#")

        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)

        list = ["male", "female"]

        combo = QComboBox()
        combo.addItems(list)

        vbox = QVBoxLayout()

        vbox.addWidget(combo)

        group_box.setLayout(vbox)
        group_box1.setLayout(vboxp)

        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        main_layout.addWidget(group_box1)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tab()
    window.show()
    app.exec()