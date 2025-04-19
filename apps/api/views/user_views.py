from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.UserSerializers import UserSerializer
from apps.core.models import User


@api_view(['GET'])
def user_list_view(request):
    user_list = User.objects.prefetch_related('group_members').all()
    serializer = UserSerializer(user_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_by_id(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def user_by_username(request, username):
#     user = User.objects.get(username=username)
#     serializer = UserSerializer(user)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
