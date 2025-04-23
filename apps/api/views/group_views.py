from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.GroupSerializer import GroupSerializer
from apps.group.models import Group


@api_view(['GET'])
def group_list_view(request):
    group_list = Group.objects.all()
    serializer = GroupSerializer(group_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def group_by_id(request, pk):
    group = Group.objects.get(pk=pk)
    serializer = GroupSerializer(group)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def group_by_slug(request, slug):
    group = Group.objects.get(slug=slug)
    serializer = GroupSerializer(group)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_group(request):
    group = GroupSerializer(data=request.data)

    if group.is_valid():
        group.save()
        return Response(data=group.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_group(request, pk):
    group = Group.objects.get(pk=pk)
    upd_group = GroupSerializer(instance=group, data=request.data)

    if upd_group.is_valid():
        upd_group.save()
        return Response(data=upd_group.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_group(request, pk):
    if Group.objects.filter(pk=pk).exists():
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        raise serializers.ValidationError('Not found this data')
