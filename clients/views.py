from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

from property import models as property_models
from property import forms as property_forms



# Create your views here.

@login_required(login_url='account_login')
def dashboard(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile is none")
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')
    profile = request.user.profile
    properties = property_models.Property_data.objects.filter(user=request.user)
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




# Properties **********************************************************************
@ login_required(login_url='account_login')
def property_all_list(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile is none")
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')
    profile = request.user.profile
    properties = property_models.Property_data.objects.filter(user=request.user)
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
    return render(request, "clients/pages/properties_all_list.html", data )



@ login_required(login_url='account_login')
def property_own_list(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile is none")
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')
    profile = request.user.profile
    properties = property_models.Property_data.objects.all()
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
    return render(request, "clients/pages/properties_all_list.html", data )







@ login_required(login_url='account_login')
def property_create(request):
    form = property_forms.PropertyForm()
    print('property_create')
    if request.method == 'POST':
        print('property_create_post')
        print(request.POST)
        form = property_forms.PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            print('form valid')
            form = form.save(commit=False)
            form.user = request.user

            form.save()
            return redirect( 'clients:property_all_list')
    context = {'form': form}
    return render(request, 'clients/pages/property_add.html', context)




@ login_required(login_url='account_login')
def property_update(request,  property_id):
    print('property_update', property_id)
    property_data = property_models.Property_data.objects.get(id=property_id)
    form = property_forms.PropertyForm(instance=property_data)
    if request.method == 'POST':
        form = property_forms.PropertyForm(request.POST, request.FILES,
                            instance=property_data)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('property:property_all')

    context = {
        'property_data': property_data,
        'form': form,

    }
    return render(request, 'property/property_update.html', context)


# portions **********************************************************************


@login_required(login_url='account_login')
def portions_all_list(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile is none")
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')
    profile = request.user.profile
    portions = property_models.Portions.objects.filter(user=request.user)
    print('portions')
    print(portions)  
    data = {
        'profile' : profile,
        'portions': portions, 
        }
    return render(request, "clients/pages/portions_all_list.html", data )


@login_required(login_url='account_login')
def portions_own_list(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile is none")
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')
    profile = request.user.profile
    portions = property_models.Portions.objects.filter(user=request.user)
    print('portions')
    print(portions)  
    data = {
        'profile' : profile,
        'portions': portions, 
        }
    return render(request, "clients/pages/portions_all_list.html", data )


@login_required(login_url='account_login')
def portions_a_building(request, property_id):
    
    property = get_object_or_404(property_models.Property_data, id=property_id)
    
    profile = request.user.profile
    portions = property_models.Portions.objects.filter(user=request.user, property_data_id=property_id)
    print('portions')
    print(portions)  
    data = {
        'profile' : profile,
        'property': property, 
        'portions': portions, 
        }
    return render(request, "clients/pages/portions_all_list.html", data )


@ login_required(login_url='account_login')
def portions_add(request, property_id):
    if property_id == None:
        print('property_id is none')
        return redirect('property:dashboard')
    building = get_object_or_404(property_models.Property_data, id=property_id)
    if building.user != request.user:
        messages.error(request, 'You are not authorized to access this portion.', extra_tags='danger')
        return redirect('property:dashboard')
    form = property_forms.PortionsForm()
    print('portion_single_add')
    if request.method == 'POST':
        form = property_forms.PortionsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            print('form valid')
            form.property_data_id = property_id
            form.user = request.user

            form.save()

            return redirect('property:portions_of_property', pk=request.user.id, property_id=property_id)
    context = {'form': form}


    return render(request, 'clients/pages/portions_add.html', context)


# @todo portions listing
@login_required(login_url='account_login')
def portions_update(request, pk, property_id, portion_id):
    all_portions = get_object_or_404(
        property_models.Portions, id=portion_id, property_data_id=property_id)
    print(all_portions)
    form = property_forms.PortionsForm(instance=all_portions)
    if request.method == 'POST':
        form = property_forms.PortionsForm(request.POST, request.FILES,
                            instance=all_portions)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('property:portions_of_property', pk, property_id)
    context = {
        'form': form,

    }
    return render(request, 'property/portion_add.html', context)


# Portion Status Views **********************************************************************

@login_required(login_url='account_login')
def portions_vacant_soon(request):
    """Display portions that will be vacant soon (status pending or expiring within 30 days)"""
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')

    profile = request.user.profile
    # Get portions with vacant_soon status
    portions = property_models.Portions.objects.filter(
        user=request.user,
        portions_status__status='vacant_soon'
    ).distinct()

    data = {
        'profile': profile,
        'portions': portions,
        'filter_type': 'Vacant Soon',
    }
    return render(request, "clients/pages/portions_all_list.html", data)


@login_required(login_url='account_login')
def portions_vacants(request):
    """Display vacant portions (status vacant)"""
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')

    profile = request.user.profile
    # Get vacant portions
    portions = property_models.Portions.objects.filter(
        user=request.user,
        portions_status__status='vacant'
    ).distinct()

    data = {
        'profile': profile,
        'portions': portions,
        'filter_type': 'Vacant',
    }
    return render(request, "clients/pages/portions_all_list.html", data)


@login_required(login_url='account_login')
def portions_occupied(request):
    """Display occupied portions (status occupied)"""
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')

    profile = request.user.profile
    # Get occupied portions
    portions = property_models.Portions.objects.filter(
        user=request.user,
        portions_status__status='occupied'
    ).distinct()

    data = {
        'profile': profile,
        'portions': portions,
        'filter_type': 'Occupied',
    }
    return render(request, "clients/pages/portions_all_list.html", data)


@login_required(login_url='account_login')
def portions_unlisted(request):
    """Display unlisted portions (not listed for rent/sale)"""
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        return redirect('accounts:profile')
    if request.user.profile.is_business == False:
        messages.error(request, 'You are not authorized to access Property Dashboard.', extra_tags='danger')
        return redirect('accounts:profile')

    profile = request.user.profile
    # Get unlisted portions (those without any status)
    portions = property_models.Portions.objects.filter(
        user=request.user,
        portions_status__isnull=True
    )

    data = {
        'profile': profile,
        'portions': portions,
        'filter_type': 'Unlisted',
    }
    return render(request, "clients/pages/portions_all_list.html", data)
