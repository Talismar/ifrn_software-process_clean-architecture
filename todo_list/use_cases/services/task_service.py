from todo_list.core.entities.task import Task
from todo_list.core.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, title, description):
        task = Task(id=None, title=title, description=description)
        return self.task_repository.create_task(task.title, task.description)

    def mark_task_as_completed(self, task_id):
        task = self.task_repository.get_task_by_id(task_id)
        if task:
            self.task_repository.mark_task_as_completed(task_id)
        return task

    def get_task_by_id(self, task_id):
        return self.task_repository.get_task_by_id(task_id)

    def list_tasks(self):
        return self.task_repository.list_tasks()
