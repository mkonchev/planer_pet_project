from rest_framework import serializers, status
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


@api_view(['POST'])
def add_task(request):
    task = TaskSerializer(data=request.data)

    if task.is_valid():
        task.save()
        return Response(data=task.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    upd_task = TaskSerializer(instance=task, data=request.data)

    if upd_task.is_valid():
        upd_task.save()
        return Response(data=upd_task.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_task(request, pk):
    if Task.objects.filter(pk=pk).exists():
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        raise serializers.ValidationError('Not found this data')
