from django.http import HttpRequest
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.froms import RegisterForm

import json 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        if user.name:
            token['name'] = user.name
        token['admin'] = user.is_staff
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def register_view(request: HttpRequest):
    data = (json.loads( request.body.decode()))
    form = RegisterForm(data)

    if form.is_valid():
        form.save()
    else:
        return Response(form.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
    return Response(data)