from abc import ABC, abstractmethod


class TaskRepository(ABC):
    @abstractmethod
    def get_task_by_id(self, task_id):
        pass

    @abstractmethod
    def create_task(self, title, description):
        pass

    @abstractmethod
    def mark_task_as_completed(self, task_id):
        pass

    @abstractmethod
    def list_tasks(self):
        pass
