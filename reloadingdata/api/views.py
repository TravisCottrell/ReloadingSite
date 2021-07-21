from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_protect

from mydata.models import Gun, Bullet, TestResult, Velocity
from api.serializers import GunSerializer, BulletSerializer, TestResultSerializer, VelocitySerializer 

@login_required
@api_view(['GET','POST'])
def guns_list(request):
    """
    List all guns, or create a new gun.
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

@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def gun_detail(request, pk):
    """
    Retrieve, update or delete a gun.
    """
    try:
        gun = Gun.objects.filter(owner=request.user, id=pk).prefetch_related('bullets__results__velocity')
        #gun = Gun.objects.get(owner=request.user, id=pk)
    except Gun.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GunSerializer(gun, many=True)
        return Response(serializer.data)


@login_required
@api_view(['POST'])
def result_create(request, pk):
    """
    new blank result
    """
    #get the bullet that the results will be related to
    bullet = Bullet.objects.get(pk=pk)
    
    #result and velocity data that will be used to make a new blank result
    data = {
        'charge':0,
        'moa':0,
        'velocity':[
            {'shotnumber':1 ,'velocity':0},
            {'shotnumber':2,'velocity':0},
            {'shotnumber':3, 'velocity':0},
        ],
    }

    serializer = TestResultSerializer(data=data, context={'bullet':bullet}, partial=True)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['PUT'])
def result_update(request, pk):
    """
    Update an existing result 
    """
    
    result = TestResult.objects.get(pk=pk)
    serializer = TestResultSerializer(result, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required    
@api_view(['DELETE'])
def result_delete(request, pk):
    """
    delete a result
    """
    
    result = TestResult.objects.get(pk=pk)
    result.delete()
   
    return JsonResponse("result deleted", safe=False)

    

