import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from property import forms as property_forms
from property import models as property_models
from PIL import Image
from django.contrib import messages
from dateutil.relativedelta import relativedelta
# Create your views here.




@login_required(login_url='account_login')
def building_all(request):
    if User:
        pk = request.user.id
        properties = property_models.Building_data.objects.all()
        print(properties)
        portions_count = properties.annotate(number_of_portions=Count('portions')).values('id', 'number_of_portions')
        print('portions_count')
        print(portions_count)
        portions_status = property_models.Portions.objects.all().annotate(status=Count('portions_status')).values('id', 'status')
        print('portions_status')
        print(portions_status)



        
        context = {
            'properties': properties,
            'portions_count': portions_count,
        }
        return render(request,  'property/building_all.html', context)
    return render(request, "property/")


# buildingss *********************************************************************
@ login_required(login_url='account_login')
def building_own(request, pk):
    building_own = property_models.Building_data.objects.filter(user_id=pk)

    context = {
        'building_own': building_own,
        'pk': pk
    }
    return render(request, 'property/building_own.html', context)


@ login_required(login_url='account_login')
def building_create(request, pk):
    form = property_forms.BuildingForm()
    if request.method == 'POST':
        form = property_forms.BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()
            return redirect('property:building_own', pk=request.user.id)
    context = {'form': form}
    return render(request, 'property/building_add.html', context)


@ login_required(login_url='account_login')
def building_plus_portion_create(request, pk):
    building_form = property_forms.BuildingForm()
    portion_form = property_forms.PortionsForm()
    single_form = property_forms.Singelform()
    if request.method == 'POST':
        building_form = property_forms.BuildingForm(request.POST, request.FILES)
        portion_form = property_forms.PortionsForm(request.POST, request.FILES)
        if building_form.is_valid() and portion_form.is_valid():
            building = building_form.save(commit=False)
            building.user = request.user
            building.save()
            
            portion = portion_form.save(commit=False)
            portion.building_data = building
            portion.user = request.user
            portion.save()
            
            return redirect('property:building_own', pk=request.user.id)
    context = {
        'building_form': building_form,
        'portion_form': portion_form,
        'single_form': single_form,
    }
    return render(request, 'property/building_plus_portion_add.html', context)


@ login_required(login_url='account_login')
def building_update(request, pk, building_id):
    print('building_update', building_id)
    building_data = property_models.Building_data.objects.get(id=building_id)
    form = property_forms.BuildingForm(instance=building_data)
    if request.method == 'POST':
        form = property_forms.BuildingForm(request.POST, request.FILES,
                            instance=building_data)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('property:building_all')

    context = {
        'building_data': building_data,
        'form': form,

    }
    return render(request, 'property/building_update.html', context)


# portions  *********************************************************************
@ login_required(login_url='account_login')
def portions_list_all(request, pk):
    pk = pk
    user_id = request.user.id
    portions_list_all = property_models.Portions.objects.all()

    context = {
        'portions': portions_list_all,
        'pk': pk,
        'user_id': user_id
    }
    return render(request, 'property/portions_list_all.html', context)


@ login_required(login_url='account_login')
def portions_of_building(request, pk, building_id):
    pk = pk
    user_id = request.user.id
    portions_of_building = property_models.Portions.objects.filter(
        Q(building_data_id=building_id) & Q(user_id=pk))

    context = {
        'portions': portions_of_building,
        'building_id': building_id,
        'pk': pk,
        'user_id': user_id
    }
    return render(request, 'property/portions_of_building.html', context)


@ login_required(login_url='account_login')
def portions_own_buildings(request, pk):
    user_id = request.user.id
    portion_all = property_models.Portions.objects.all().filter(user_id=pk)
    print(portion_all)


    context = {
        'portions': portion_all,
        'user_id': user_id
    }
    return render(request, 'property/portions_own_buildings.html', context)


@ login_required(login_url='account_login')
def portion_single_details(request, pk, building_id, portion_id):
    pk = request.user.id
    print(pk)

    print(portion_id)
    portion = property_models.Portions.objects.get(id=portion_id)
    print(portion)

    context = {
        'portion': portion
    }
    return render(request, 'property/portion_single_details.html', context)


@ login_required(login_url='account_login')
def portion_single_add(request, pk, building_id):
    form = property_forms.PortionsForm()
    print('portion_single_add')
    if request.method == 'POST':
        form = property_forms.PortionsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            print('form valid')
            form.building_data_id = building_id
            form.user_id = pk

            form.save()

            return redirect('property:portions_of_building', pk, building_id)
    context = {'form': form}


    return render(request, 'property/portion_single_add.html', context)


# @todo portions listing
@login_required(login_url='account_login')
def portion_single_update(request, pk, building_id, portion_id):
    all_portions = get_object_or_404(
        property_models.Portions, id=portion_id, building_data_id=building_id)
    print(all_portions)
    form = property_forms.PortionsForm(instance=all_portions)
    if request.method == 'POST':
        form = property_forms.PortionsForm(request.POST, request.FILES,
                            instance=all_portions)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('property:portions_of_building', pk, building_id)
    context = {
        'form': form,

    }
    return render(request, 'property/portion_single_update.html', context)


@login_required(login_url='account_login')
def portion_status_list(request, pk, building_id):

    building = property_models.Building_data.objects.get(id=building_id)

    print(pk)
    print(building_id)
    portion_all = property_models.Portions.objects.filter(
        Q(building_data_id=building_id) & Q(user_id=pk)).all()
    print(portion_all)

    context = {
        'portion_all': portion_all,
        'pk': pk,
        'building': building,
        'building_id': building_id,
    }
     
    return render(request, 'property/portion_status_list.html', context )

@login_required(login_url='account_login')
def vacant_status_update(request, portion_id):
    pk = request.user.id
    # Get the parent Portions instance to link and to get building_id
    actual_portion_object = get_object_or_404(property_models.Portions, id=portion_id)
    building_id = actual_portion_object.building_data_id

    # Calculate the first day of the next month
    today = datetime.date.today()
    first_day_next_month = (today + relativedelta(months=1)).replace(day=1)

    # Get or create the Portions_status instance
    # This ensures status_instance is always a saved instance, either existing or newly created.
    status_instance, created = property_models.Portions_status.objects.get_or_create(
        portions=actual_portion_object,  # Link using the Portions object itself
        defaults={'status': 'NOT_SET', 'vacant_date': first_day_next_month}
    )

    if request.method == 'POST':
        # For POST requests, bind the form to the submitted data and the instance
        form = property_forms.PortionsStatusForm(request.POST, instance=status_instance)
        if form.is_valid():
            # The 'portions' field is excluded from the form,
            # so form.save() will update status_instance without needing to set portions_id manually,
            # as status_instance is already correctly linked.
            form.save()
            messages.success(request, "Status updated successfully.")
            return redirect('property:portion_status_list', pk=pk, building_id=building_id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:  # GET request
        # For GET requests, initialize the form with the instance data
        form = property_forms.PortionsStatusForm(instance=status_instance)

    context = {
        'form': form,
        'portion_id': portion_id, # Pass for template use if needed (e.g., in URLs)
        'actual_portion_object': actual_portion_object, # Pass for context if needed in template
    }
    return render(request, 'property/portion_status_update.html', context)


# inquire ...........................................................
 
def inquire_create(request):
    form = property_forms.InquireForm()
    if request.method == 'POST':
        form = property_forms.InquireForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            print(form)
            form.save()
            return redirect('property:building_all')
    context = {'form': form}
    return render(request, 'property/inquire_add.html', context)


@login_required(login_url='account_login')
def inquire_lists(request):
    pk = request.user.id
    inquires = property_models.Inquire.objects.all()
    if not request.user.profile.is_realtor:
        print('not realtor')
        messages.info(request, 'Access to the inquiries list is restricted to realtors only.')
        return redirect('webpages:home')
    data = {
        'inquires': inquires,
    }
    return render(request,  'property/inquire_lists.html', data)
