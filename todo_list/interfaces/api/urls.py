from django.urls import path
from todo_list.use_cases.services.task_service import TaskService
from todo_list.adapters.database.task_db_repository import TaskDbRepository
from todo_list.interfaces.api.views.task_views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
)


task_repo = TaskDbRepository()
task_service = TaskService(task_repo)


urlpatterns = [
    path(
        "tasks/",
        TaskListCreateView.as_view(service=task_service),
        name="task-list-create",
    ),
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDestroyView.as_view(service=task_service),
        name="task-retrieve-update-destroy",
    ),
]
