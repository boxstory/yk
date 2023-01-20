from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from property.forms import *
from property.models import *
from PIL import Image
# Create your views here.


@login_required(login_url='account_login')
def property_all(request):
    if User:
        pk = request.user.id
        properties = Building_info.objects.all()
        portions_count = Building_info.objects.annotate(
            number_of_portions=Count('portions'))
        data = {
            'properties': properties,
            'portions_count': portions_count,
        }
        return render(request,  'property/building_all.html', data)
    return render(request, "property/")

# buildingss *********************************************************************


@ login_required(login_url='account_login')
def own_building(request, pk):
    own_building = Building_info.objects.filter(user_id=pk)

    context = {
        'own_building': own_building,
        'pk': pk
    }
    return render(request, 'property/own_building.html', context)


@ login_required(login_url='account_login')
def building_create(request, pk):
    form = BuildingForm()
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()
            return redirect('property:own_building', pk=request.user.id)
    context = {'form': form}
    return render(request, 'property/building_create.html', context)


@ login_required(login_url='account_login')
def building_update(request, pk, building_id):
    print('building_update', building_id)
    building_info = Building_info.objects.get(id=building_id)
    form = BuildingForm(instance=building_info)
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES,
                            instance=building_info)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('property:property_all')

    context = {
        'building_info': building_info,
        'form': form,

    }
    return render(request, 'property/building_update.html', context)

# portions  *********************************************************************


@ login_required(login_url='account_login')
def portion_all(request, pk, building_id):
    pk = pk
    user_id = request.user.id
    portion_all = Portions.objects.filter(
        Q(building_info_id=building_id) & Q(user_id=pk))

    context = {
        'portions': portion_all,
        'building_id': building_id,
        'pk': pk,
        'user_id': user_id
    }
    template = 'property/portion_all.html'
    return render(request, template, context)


@ login_required(login_url='account_login')
def portion_single(request, pk, building_id, portion_id):
    pk = request.user.id
    print(pk)

    print(portion_id)
    portion = Portions.objects.get(id=portion_id)
    print(portion)

    context = {
        'portion': portion
    }
    template = 'property/portion_single.html'
    return render(request, template, context)


@ login_required(login_url='account_login')
def portion_add(request, pk, building_id):
    form = PortionsForm()
    if request.method == 'POST':
        form = PortionsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.building_info_id = building_id
            print(form)
            form.save()

            return redirect('property:portion_all', pk, building_id)
    context = {'form': form}
    return render(request, 'property/portion_add.html', context)

# @toto portions listing


@login_required(login_url='account_login')
def portion_update(request, pk, building_id, portion_id):
    all_portions = get_object_or_404(
        Portions, id=portion_id)
    print(all_portions)
    form = PortionsForm(instance=all_portions)
    if request.method == 'POST':
        form = PortionsForm(request.POST, request.FILES,
                            instance=all_portions)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('property:portion_all', pk, building_id)
    context = {
        'form': form,

    }
    return render(request, 'property/building_update.html', context)


@login_required(login_url='account_login')
def vacant_status(request, pk, building_id, portion_id):

    print(pk)
    print(building_id)
    print(portion_id)
    portion_all = Portions.objects.filter(
        Q(building_info_id=building_id) & Q(user_id=pk)).first()
    print(portion_all)
    form = PortionsStatusForm()
    if request.method == 'POST':
        form = PortionsStatusForm(request.POST,
                                  instance=portion_all)
        print('form post')
        if form.is_valid():
            print('form VALID')
            form = form.save(commit=False)
            form.portions_id = portion_id
            print(form.portions_id)
            form.save()
            print(form)
            return redirect('property:portion_all', pk, building_id)
    context = {
        'form': form,

    }
    return render(request, 'property/portion_vacant_update.html', context)


# inquire ...........................................................

def inquire_create(request):
    form = InquireForm()
    if request.method == 'POST':
        form = InquireForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            print(form)
            form.save()
            return redirect('property:property_all')
    context = {'form': form}
    return render(request, 'property/inquire_create.html', context)


@login_required(login_url='account_login')
def inquire_lists(request):
    pk = request.user.id
    inquires = Inquire.objects.all()
    print(Inquire)
    data = {
        'inquires': inquires,
    }
    return render(request,  'property/inquire_lists.html', data)
