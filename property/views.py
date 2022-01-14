from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from property.forms import PropertyForm
from property.models import *

# Create your views here.


@login_required(login_url='account_login')
def propertyindex(request):
    if User:
        pk = request.user.id
        properties = Property.objects.all()
        template = f"/property/{pk}"
        data = {
            'properties': properties
        }
        return render(request,  'property/index.html', data)
    return render(request, "property/")


@login_required(login_url='account_login')
def own_properties(request, pk):

    pk = request.user.id
    print(pk)
    own_properties = Property.objects.filter(user_id=pk)
    print(own_properties)

    context = {
        'own_properties': own_properties,
        'pk': pk
    }
    return render(request, 'property/own_properties.html', context)


@login_required(login_url='account_login')
def property_create(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return render(request, 'property/property_create.html')
    context = {'form': form}
    return render(request, 'property/property_create.html', context)


@login_required(login_url='account_login')
def property_update(request, pk):
    own_properties = get_object_or_404(Property, user_id=pk)
    print(own_properties)
    property_id_lists = []
    for property in own_properties:
        print(pk)
        print(property.id)
        property_id_lists.append(property.id)
        print(property_id_lists)
        id = property.id
        print(id)
        property_status = Property_info.objects.filter(id=id)
        print(property_status)

    context = {
        'own_properties': own_properties,
        'property_status': property_status,
    }
    return render(request, 'property/property_update.html', context)


@login_required(login_url='account_login')
def single_property(request, pk, property_id):
    pk = request.user.id
    print(pk)

    print(property_id)
    single_property = Property.objects.filter(user_id=pk)
    print(single_property)

    context = {
        'single_property': single_property
    }
    template = 'property/single_property.html'
    return render(request, template, context)
