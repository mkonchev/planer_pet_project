from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.serializers.StoreSerializer import StoreSerializer
from apps.store.models import Store


@api_view(['GET'])
def store_list_view(request):
    store_list = Store.objects.all()
    serializer = StoreSerializer(store_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def store_by_id(request, pk):
    store = Store.objects.get(pk=pk)
    serializer = StoreSerializer(store)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_store(request):
    store = StoreSerializer(data=request.data)

    if store.is_valid():
        store.save()
        return Response(data=store.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_store(request, pk):
    store = Store.objects.get(pk=pk)
    upd_store = StoreSerializer(instance=store, data=request.data)

    if upd_store.is_valid():
        upd_store.save()
        return Response(data=upd_store.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_store(request, pk):
    if Store.objects.filter(pk=pk).exists():
        store = Store.objects.get(pk=pk)
        store.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        raise serializers.ValidationError('Not found this data')
