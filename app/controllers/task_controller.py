from app.services.task_service import TaskService

class TaskController:
    def __init__(self):
        self.service = TaskService()

    def list_tasks(self):
        return self.service.get_all_tasks()

    def create_task(self, title, priority):
        self.service.add_task(title, priority)

    def toggle_task(self, index):
        self.service.toggle_complete(index)

    def delete_task(self, index):
        self.service.delete_task(index)
