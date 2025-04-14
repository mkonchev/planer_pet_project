from rest_framework import serializers

from apps.core.models import User
from apps.group.models import Group


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Group
        fields = '__all__'
