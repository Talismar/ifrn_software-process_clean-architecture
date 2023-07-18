from rest_framework import generics
from rest_framework.response import Response
from todo_list.use_cases.services.task_service import TaskService
from todo_list.adapters.database.task_db_repository import TaskDbRepository
from todo_list.interfaces.api.serializers.task_serializer import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    service: TaskService = None

    def get_queryset(self):
        return self.service.list_tasks()

    def perform_create(self, serializer):
        task_data = serializer.validated_data
        task = self.service.create_task(task_data["title"], task_data["description"])
        serializer.save(id=task.id)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    service: TaskService = None
    queryset = TaskDbRepository().list_tasks()

    def perform_update(self, serializer):
        task_data = serializer.validated_data
        task_id = self.kwargs["pk"]
        task = self.service.mark_task_as_completed(task_id)
        serializer.save(completed=task.completed)

    def perform_destroy(self, instance):
        task_id = self.kwargs["pk"]
        self.service.delete_task(task_id)
