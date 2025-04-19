from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.MembershipSerializer import MembershipSerializer
from apps.membership.models import Membership


@api_view(['GET'])
def membership_list_view(request):
    membership_list = Membership.objects.all()
    serializer = MembershipSerializer(membership_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def membership_by_id(request, pk):
    membership = Membership.objects.get(pk=pk)
    serializer = MembershipSerializer(membership)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
