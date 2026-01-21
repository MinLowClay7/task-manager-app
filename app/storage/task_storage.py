import json
import os

class TaskStorage:
    FILE_PATH = "tasks.json"

    @classmethod
    def load_tasks(cls):
        if not os.path.exists(cls.FILE_PATH):
            return []

        with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    @classmethod
    def save_tasks(cls, tasks):
        with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
