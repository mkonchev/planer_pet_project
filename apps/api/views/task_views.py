from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.TaskSerializer import TaskSerializer
from apps.task.models import Task


@api_view(['GET'])
def task_list_view(request):
    task_list = Task.objects.all()
    serializer = TaskSerializer(task_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def task_by_id(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
