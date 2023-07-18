from .models import TaskModel
from todo_list.core.repositories.task_repository import TaskRepository
from todo_list.core.entities.task import Task


class TaskDbRepository(TaskRepository):
    def get_task_by_id(self, task_id):
        try:
            task_model = TaskModel.objects.get(pk=task_id)
            return self._decode_task_model(task_model)
        except TaskModel.DoesNotExist:
            return None

    def create_task(self, title, description):
        task_model = TaskModel.objects.create(title=title, description=description)
        return self._decode_task_model(task_model)

    def mark_task_as_completed(self, task_id):
        task_model = TaskModel.objects.get(pk=task_id)
        task_model.completed = True
        task_model.save()

    def list_tasks(self):
        task_models = TaskModel.objects.all()
        return [self._decode_task_model(task_model) for task_model in task_models]

    def _decode_task_model(self, task_model: TaskModel):
        return Task(
            id=task_model.id,
            title=task_model.title,
            description=task_model.description,
            completed=task_model.completed,
        )
