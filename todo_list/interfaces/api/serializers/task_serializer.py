from rest_framework import serializers
from todo_list.core.entities.task import Task


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task(**validated_data)
