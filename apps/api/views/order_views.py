from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.OrderSerializer import OrderSerializer
from apps.order.models import Order


@api_view(['GET'])
def order_list_view(request):
    order_list = Order.objects.all()
    serializer = OrderSerializer(order_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def order_by_id(request, pk):
    order = Order.objects.get(pk=pk)
    serializer = OrderSerializer(order)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_order(request):
    order = OrderSerializer(data=request.data)

    if order.is_valid():
        order.save()
        return Response(data=order.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    upd_order = OrderSerializer(instance=order, data=request.data)

    if upd_order.is_valid():
        upd_order.save()
        return Response(data=upd_order.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_order(request, pk):
    if Order.objects.filter(pk=pk).exists():
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        raise serializers.ValidationError('Not found this data')
