from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.StoreSerializer import StoreSerializer
from apps.store.models import Store


@api_view(['GET'])
def store_list_view(request):
    store_list = Store.objects.all()
    serializer = StoreSerializer(store_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
