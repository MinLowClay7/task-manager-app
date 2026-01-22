import sys
import os
from PySide6.QtWidgets import QApplication, QLabel
from app.ui.main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/icon.png"))
    load_styles(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

def load_styles(app):
    style_path = resource_path("app/ui/styles.qss")

    with open(style_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())


def show_error(self, message):
    QMessageBox.critical(
        None,
        "Error",
        message
    )

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    main()

