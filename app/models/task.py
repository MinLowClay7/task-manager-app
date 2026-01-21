from datetime import datetime

class Task:
    def __init__(self, title, priority="Media", completed=False, created_at=None):
        self.title = title
        self.priority = priority
        self.completed = completed
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            priority=data.get("priority", "Media"),
            completed=data.get("completed", False),
            created_at=data.get("created_at")
        )
