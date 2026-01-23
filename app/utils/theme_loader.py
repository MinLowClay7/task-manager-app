import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def load_styles(theme):
    file_name = "light.qss" if theme == "light" else "dark.qss"
    path = resource_path(f"app/ui/{file_name}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
