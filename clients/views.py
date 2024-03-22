from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    profile = request.GET.get('profile')
    data = {
        'profile' : profile
    }
    return render(request, "clients/dashboard.html", data )