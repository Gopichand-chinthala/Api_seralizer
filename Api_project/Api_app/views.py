# myapp/views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

def item_htmmllist(request):
    """
    List all items.
    """
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

@api_view(['GET'])
def item_list(request):
    """
    List all items.
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def item_create(request):
    """
    Create a new item.
    """
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def item_delete(request, pk):
    """
    Delete an item.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
