from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QComboBox, QMessageBox
)

class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear tarea")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.input_title = QLineEdit()
        self.input_title.setPlaceholderText("Título de la tarea")

        self.priority_box = QComboBox()
        self.priority_box.addItems(["Alta", "Media", "Baja"])

        btn_save = QPushButton("Guardar")
        btn_save.clicked.connect(self.validate)

        layout.addWidget(QLabel("Título"))
        layout.addWidget(self.input_title)
        layout.addWidget(QLabel("Prioridad"))
        layout.addWidget(self.priority_box)
        layout.addWidget(btn_save)

        self.setLayout(layout)

    def validate(self):
        if not self.input_title.text().strip():
            QMessageBox.warning(self, "Error", "El título es obligatorio")
            return
        self.accept()

