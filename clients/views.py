from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from property import models as property_models

# Create your views here.

@login_required(login_url='account_login')
def dashboard(request):
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('account_login')
    profile = request.user.profile
    properties = property_models.Building_data.objects.filter(user=request.user)
    print('properties')
    print(properties)
    portions_count = properties.annotate(number_of_portions=Count('portions')).values('id', 'number_of_portions')
    
    print('portions_count')
    print(portions_count)
    
    data = {
        'profile' : profile,
        'properties': properties,
        'portions_count': portions_count,


    }
    return render(request, "clients/dashboard.html", data )