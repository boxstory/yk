from django.shortcuts import render
from . import views

# Create your views here.
from django.http import HttpResponse


def propertyindex(request):
    return render(request, 'property/index.html')
