from app.models.task import Task
from app.storage.task_storage import TaskStorage

class TaskService:

    def get_all_tasks(self):
        data = TaskStorage.load_tasks()
        return [Task.from_dict(item) for item in data]

    def add_task(self, title, priority):
        tasks = self.get_all_tasks()
        tasks.append(Task(title=title, priority=priority))
        self._save(tasks)

    def toggle_complete(self, index):
        tasks = self.get_all_tasks()
        tasks[index].completed = not tasks[index].completed
        self._save(tasks)

    def delete_task(self, index):
        tasks = self.get_all_tasks()
        tasks.pop(index)
        self._save(tasks)

    def _save(self, tasks):
        TaskStorage.save_tasks([t.to_dict() for t in tasks])
