from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.OrderSerializer import OrderSerializer
from apps.order.models import Order


@api_view(['GET'])
def order_list_view(request):
    order_list = Order.objects.all()
    serializer = OrderSerializer(order_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
