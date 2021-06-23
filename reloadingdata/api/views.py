from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from mydata.models import Gun, Bullet, TestResult, Velocity
from api.serializers import GunSerializer 

@api_view(['GET','POST'])
def guns_list(request):
    """
    List all code guns, or create a new gun.
    """
    if request.method == 'GET':
        guns = Gun.objects.all()
        serializer = GunSerializer(guns, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def gun_detail(request, pk):
    """
    Retrieve, update or delete a code gun.
    """
    try:
        gun = Gun.objects.get(owner=request.user, id=pk)
    except Gun.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GunSerializer(gun)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = GunSerializer(gun, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gun.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)