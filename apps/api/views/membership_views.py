from rest_framework import serializers, status
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


@api_view(['POST'])
def add_membership(request):
    membership = MembershipSerializer(data=request.data)

    if membership.is_valid():
        membership.save()
        return Response(data=membership.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_membership(request, pk):
    membership = Membership.objects.get(pk=pk)
    upd_membership = MembershipSerializer(instance=membership, data=request.data)

    if upd_membership.is_valid():
        upd_membership.save()
        return Response(data=upd_membership.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_membership(request, pk):
    if Membership.objects.filter(pk=pk).exists():
        membership = Membership.objects.get(pk=pk)
        membership.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        raise serializers.ValidationError('Not found this data')
