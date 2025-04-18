from rest_framework import serializers

from apps.api.serializers.UserSerializers import UserSerializer
from apps.group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Group
        fields = '__all__'
