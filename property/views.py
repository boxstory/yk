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
def property_all(request):
    if User:
        pk = request.user.id
        properties = property_models.Property_data.objects.all()
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
        return render(request,  'property/property_all.html', context)
    return render(request, "property/")


# propertiess *********************************************************************
@ login_required(login_url='account_login')
def property_own(request, pk):
    property_own = property_models.Property_data.objects.filter(user_id=pk)

    context = {
        'property_own': property_own,
        'pk': pk
    }
    return render(request, 'property/property_own.html', context)



@ login_required(login_url='account_login')
def property_plus_portion_create(request, pk):
    property_form = property_forms.PropertyForm()
    portion_form = property_forms.PortionsForm()
    single_form = property_forms.Singelform()
    if request.method == 'POST':
        property_form = property_forms.PropertyForm(request.POST, request.FILES)
        portion_form = property_forms.PortionsForm(request.POST, request.FILES)
        if property_form.is_valid() and portion_form.is_valid():
            building = property_form.save(commit=False)
            building.user = request.user
            building.save()
            
            portion = portion_form.save(commit=False)
            portion.property_data = building
            portion.user = request.user
            portion.save()
            
            return redirect('property:property_own', pk=request.user.id)
    context = {
        'property_form': property_form,
        'portion_form': portion_form,
        'single_form': single_form,
    }
    return render(request, 'property/property_plus_portion_add.html', context)


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
def portions_of_property(request, pk, property_id):
    pk = pk
    user_id = request.user.id
    portions_of_property = property_models.Portions.objects.filter(
        Q(property_data_id=property_id) & Q(user_id=pk))

    context = {
        'portions': portions_of_property,
        'property_id': property_id,
        'pk': pk,
        'user_id': user_id
    }
    return render(request, 'property/portions_of_property.html', context)


@ login_required(login_url='account_login')
def portions_own_properties(request, pk):
    user_id = request.user.id
    portion_all = property_models.Portions.objects.all().filter(user_id=pk)
    print(portion_all)


    context = {
        'portions': portion_all,
        'user_id': user_id
    }
    return render(request, 'property/portions_own_buildings.html', context)


@ login_required(login_url='account_login')
def portion_single_details(request, pk, property_id, portion_id):
    pk = request.user.id
    print(pk)

    print(portion_id)
    portion = property_models.Portions.objects.get(id=portion_id)
    print(portion)

    context = {
        'portion': portion
    }
    return render(request, 'property/portion_single_details.html', context)



@login_required(login_url='account_login')
def portion_status_list(request, pk, property_id):

    building = property_models.Property_data.objects.get(id=property_id)

    print(pk)
    print(property_id)
    portion_all = property_models.Portions.objects.filter(
        Q(property_data_id=property_id) & Q(user_id=pk)).all()
    print(portion_all)

    context = {
        'portion_all': portion_all,
        'pk': pk,
        'building': building,
        'property_id': property_id,
    }
     
    return render(request, 'property/portion_status_list.html', context )

@login_required(login_url='account_login')
def vacant_status_update(request, portion_id):
    pk = request.user.id
    # Get the parent Portions instance to link and to get property_id
    actual_portion_object = get_object_or_404(property_models.Portions, id=portion_id)
    property_id = actual_portion_object.property_data_id

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
            return redirect('property:portion_status_list', pk=pk, property_id=property_id)
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
            return redirect('property:property_all')
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
