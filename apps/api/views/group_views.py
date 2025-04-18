from rest_framework import status
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
