from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profiles.models import loginModel, ProfileModel
from profiles.serializers import LoginModelSerializer, ProfileModelSerializer

# Create your views here.
@api_view(['GET'])
def profiles_list(request, format=None):
    profiles = ProfileModel.objects.all()
    serializer = ProfileModelSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_profiles(request, format=None):
    print(request.data)
    serializer = ProfileModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def check_account(request, format=None):    
    serializer = LoginModelSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data['email']);

    try:
        result = loginModel.objects.get(email=serializer.data['email']);
    except loginModel.DoesNotExist:
        return Response('account is not exit')

    if(result.password != serializer.data['password']):
        return Response('password is not correct')

    return Response('OK')

    #print(result.password)
    #LoginModel.objects.get(email=serializer);
    #if serializer.is_valid():
        #serializer.save() 
    #return JsonResponse(serializer.data, status=201)
    #return JsonResponse(serializer.errors, status=400)
    