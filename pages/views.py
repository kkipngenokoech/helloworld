from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homepageview(request):
    return HttpResponse('Hello, World')