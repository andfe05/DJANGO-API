from urllib import request
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json
# Create your views here.

@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()  

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_nick(request, nick):

    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = UserSerializer(user)

        return Response(serializer.data)
    
    if request.method != 'PUT':
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_ACEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#CRUDZAO DA MASSA

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def use_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['user']:

                user_nickname = request.GET['user']
            try:
                user= User.objects.get(pk=user_nickname)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

#criando dados

def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# editando dados
@api_view(['PUT'])
def update_user(request):
    if request.method == 'PUT':

     nickname = request.data['user_nickname']

    updated_user = User.objects.get(pk=nickname)

    print(request.data)

    serializer = UserSerializer(updated_user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















def databaseEmDjango():

    data = User.objects.get(pk='andre_nick')  #OBJETO

    data = User.objects.filter(user_age='25') #QUERYSET

    data = User.objects.exclude(user_age='25') #QUERYSET

    data.save()

    data.delete()