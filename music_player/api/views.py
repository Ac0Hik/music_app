from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mn(request):
    return HttpResponse('welcome to the home page')