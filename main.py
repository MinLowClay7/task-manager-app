import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from app.ui.main_window import MainWindow
from app.utils.theme_loader import load_styles


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/icon.png"))

    app.setStyleSheet(load_styles("dark"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
