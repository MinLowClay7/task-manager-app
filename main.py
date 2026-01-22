import sys
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
    with open("app/ui/styles.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

def show_error(self, message):
    QMessageBox.critical(
        None,
        "Error",
        message
    )

if __name__ == "__main__":
    main()

