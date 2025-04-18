from rest_framework import serializers

from apps.core.models import User


class UserSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='group_members')

    class Meta:
        model = User
        fields = '__all__'
