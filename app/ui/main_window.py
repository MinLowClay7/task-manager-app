from asyncio import tasks
from tkinter import dialog
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem,
    QHeaderView
)
from app.controllers.task_controller import TaskController
from app.ui.add_task_dialog import AddTaskDialog
from PySide6.QtGui import QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.resize(900, 600)

        self._setup_ui()
        self.controller = TaskController()

    
    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Encabezado - Header
        title = QLabel("Task Manager")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        main_layout.addWidget(title)

        # Contenido principal - Main Content
        content_layout = QHBoxLayout()

        # --- tablas de tareas - Tasks Table ---
        self.tasks_table = QTableWidget()
        self.tasks_table.setColumnCount(4)
        self.tasks_table.setHorizontalHeaderLabels(
            ["Título", "Estado", "Prioridad", "Fecha"]
        )

        self.tasks_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        content_layout.addWidget(self.tasks_table, 3)

        # ---- Acciones - Actions ----
        actions_layout = QVBoxLayout()

        self.btn_add = QPushButton("➕ Crear tarea")
        self.btn_add.clicked.connect(self.open_add_task)
        self.btn_complete = QPushButton("✅ Completar")
        self.btn_complete.clicked.connect(self.complete_task)
        self.btn_edit = QPushButton("✏️ Editar")
        self.btn_edit.clicked.connect(self.edit_task)
        self.btn_delete = QPushButton("🗑️ Eliminar")
        self.btn_delete.clicked.connect(self.delete_task)


        actions_layout.addWidget(self.btn_add)
        actions_layout.addWidget(self.btn_complete)
        actions_layout.addWidget(self.btn_edit)
        actions_layout.addWidget(self.btn_delete)
        actions_layout.addStretch()

        content_layout.addLayout(actions_layout, 1)

        main_layout.addLayout(content_layout)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    # Abrir diálogo para agregar tarea
    def open_add_task(self):
        dialog = AddTaskDialog()

        if dialog.exec():
            title = dialog.input_title.text()
            priority = dialog.priority_box.currentText()

            self.controller.create_task(title, priority)
            self.load_tasks()

    # Completar tarea
    def complete_task(self):
        row = self.tasks_table.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Atención", "Selecciona una tarea")
            return

        self.controller.toggle_task(row)
        self.load_tasks()

    # Cargar tareas en la tabla
    def load_tasks(self):
        tasks = self.controller.list_tasks()
        self.tasks_table.setRowCount(len(tasks))

        for row, task in enumerate(tasks):
            status_item = QTableWidgetItem(
                "Completada" if task.completed else "Pendiente"
            )

            if task.completed:
                status_item.setBackground(QColor("#c8f7c5"))
            self.tasks_table.setItem(row, 1, status_item)
            self.tasks_table.setItem(row, 0, QTableWidgetItem(task.title))
            self.tasks_table.setItem(
                row, 1,
                QTableWidgetItem("Completada" if task.completed else "Pendiente")
            )
            self.tasks_table.setItem(row, 2, QTableWidgetItem(task.priority))
            self.tasks_table.setItem(row, 3, QTableWidgetItem(task.created_at))
            self.load_tasks()
    
    # Editar tarea (pendiente de implementar)
    def edit_task(self):
        QMessageBox.information(self, "Info", "Funcionalidad en desarrollo")

    def delete_task(self):
        row = self.tasks_table.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Atención", "Selecciona una tarea")
            return
        
        confirm = QMessageBox.question(
                    self,
                    "Confirmar",
                    "¿Eliminar esta tarea?",
                    QMessageBox.Yes | QMessageBox.No
                )

        if confirm == QMessageBox.Yes:
            self.controller.delete_task(row)
            self.load_tasks()
