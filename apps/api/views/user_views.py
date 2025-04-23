from rest_framework import serializers, status
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


@api_view(['POST'])
def add_user(request):
    user = UserSerializer(data=request.data)

    if user.is_valid():
        user.save()
        return Response(data=user.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    upd_user = UserSerializer(instance=user, data=request.data)

    if upd_user.is_valid():
        upd_user.save()
        return Response(data=upd_user.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_user(request, pk):
    if User.objects.filter(pk=pk).exists():
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        raise serializers.ValidationError('Not found this data')
