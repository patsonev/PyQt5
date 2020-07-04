from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit, QFontDialog, QColorDialog
import sys
from PyQt5 import QtGui


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "This is first thing"
        self.height = 700
        self.width = 1100
        self.top = 100
        self.left = 200
        self.iconName = "plioky.ico"
        self.text_edit = QTextEdit(self)

        self.init_window()
        self.create_text_editor()
        self.create_menu()

    def init_window(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def create_menu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        edit_menu = main_menu.addMenu("Edit")
        view_manu = main_menu.addMenu("View")
        help_menu = main_menu.addMenu("Help")

        copy_action = QAction(QtGui.QIcon(self.iconName), "Copy", self)
        copy_action.setShortcut("Ctrl+f")
        file_menu.addAction(copy_action)

        cut_action = QAction(QtGui.QIcon(self.iconName), "Cut", self)
        cut_action.setShortcut("Ctrl+z")
        file_menu.addAction(cut_action)

        save_action = QAction(QtGui.QIcon(self.iconName), "Save", self)
        save_action.setShortcut("Ctrl+e")
        file_menu.addAction(save_action)

        exit_action = QAction(QtGui.QIcon(self.iconName), "Exit", self)
        exit_action.setShortcut("Shift+x")
        edit_menu.addAction(exit_action)
        exit_action.triggered.connect(sys.exit)

        font_action = QAction(QtGui.QIcon(""), "Font", self)
        font_action.setShortcut("Ctrl+s")
        font_action.triggered.connect(self.font_dialog)
        view_manu.addAction(font_action)

        color_action = QAction(QtGui.QIcon(self.iconName), "Color", self)
        color_action.setShortcut("Ctrl+o")
        color_action.triggered.connect(self.color_dialog)
        edit_menu.addAction(color_action)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copy_action)
        toolbar.addAction(exit_action)
        toolbar.addAction(save_action)
        toolbar.addAction(cut_action)
        toolbar.addAction(font_action)
        toolbar.addAction(color_action)

    def create_text_editor(self):
        self.setCentralWidget(self.text_edit)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.text_edit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.text_edit.setTextColor(color)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())