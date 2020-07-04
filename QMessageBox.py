from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox, QAction, QTextEdit, QFontDialog, QColorDialog\
    , QFileDialog
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


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

        print_action = QAction(QtGui.QIcon(""), "Print", self)
        print_action.setShortcut("Shift+w")
        print_action.triggered.connect(self.print_dialog)
        file_menu.addAction(print_action)

        export_pdf_action = QAction(QtGui.QIcon(""), "Export as PDF", self)
        export_pdf_action.triggered.connect(self.pdf_export)
        file_menu.addAction(export_pdf_action)

        print_preview_action = QAction(QtGui.QIcon(""), "Preview", self)
        print_preview_action.triggered.connect(self.preview_dialog)
        help_menu.addAction(print_preview_action)

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

        help_action = QAction(QtGui.QIcon(self.iconName), "About", self)
        help_action.triggered.connect(self.about_message_box)
        help_menu.addAction(help_action)

        choice_action = QAction(QtGui.QIcon(self.iconName), "Choice message", self)
        choice_action.triggered.connect(self.question_message_box)
        help_menu.addAction(choice_action)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copy_action)
        toolbar.addAction(exit_action)
        toolbar.addAction(save_action)
        toolbar.addAction(cut_action)
        toolbar.addAction(font_action)
        toolbar.addAction(color_action)
        toolbar.addAction(print_action)
        toolbar.addAction(print_preview_action)
        toolbar.addAction(export_pdf_action)
        toolbar.addAction(help_action)

    def create_text_editor(self):
        self.setCentralWidget(self.text_edit)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.text_edit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.text_edit.setTextColor(color)

    def print_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.text_edit.print_(printer)

    def preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.print_preview)
        preview_dialog.exec_()

    def print_preview(self, printer):
        self.text_edit.print_(printer)

    def pdf_export(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files ().pdf;;All Files()")

        if fn != "":
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.text_edit.document().print_(printer)

    def about_message_box(self):
        message = QMessageBox.about(self, "About application", "This is simple text editor application")

    def question_message_box(self):
        message = QMessageBox.question(self, "Question application", "What is your choice?", QMessageBox.Yes |\
                                        QMessageBox.No)
        if message == QMessageBox.Yes:
            self.text_edit.setText("Yes I like PyQt5")
        else:
            self.text_edit.setText("No I don't like it")


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    sys.exit(myapp.exec())