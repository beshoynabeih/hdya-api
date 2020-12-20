from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


def password_reset_page(request):
    uid = request.GET['uid']
    token = request.GET['token']
    return HttpResponse("hello " + uid + "<br>" + token)

