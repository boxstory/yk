from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def dashboard(request):
    if request.user.profile.is_workman == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.')
        return redirect('account_login')
    profile = request.GET.get('profile')
    data = {
        'profile' : profile
    }
    return render(request, "clients/dashboard.html", data )