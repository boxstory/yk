from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView
from datetime import date
from webpages.form import ContactForm, SubscribeForm, CareersApplicationForm , CareersAddForm
from webpages import models as webpage_models
from accounts import models as accounts_models
# Create your views here.


def home(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscribeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            name1 = form.cleaned_data['name']
            mobile_no1 = form.cleaned_data['mobile_no']
            p = webpage_models.MobSubscriber(name=name1, mobile_no=mobile_no1,
                              date_subscribed=date.today())
            p.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/whatsapp_group/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
    
    
    
    # context = {'form': form}
    return render(request, 'webpages/home.html', {'form': form}) 
    # return render(request, 'webpages/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Form submission successful')
            return redirect('webpages:services')

        return HttpResponseRedirect(request.path_info)
    form = ContactForm()
    context = {'form': form}

    return render(request, 'webpages/contact.html', context)


def join_leads(request):
    print("join_leads")
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Form submission successful')
            return redirect('accounts:signup')

        return HttpResponseRedirect(request.path_info)
    form = SubscribeForm()
    context = {'form': form}

    return render(request, 'webpages/join_leads.html', context)


def services(request):
    return render(request, 'webpages/services.html')

#@todo





def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Form submission successful')

        return HttpResponseRedirect(request.path_info)
    form = ContactForm()
    context = {'form': form}
    return render(request, 'webpages/about.html', context)


def robots(request):
    context = {}
    return render(request, 'webpages/robots.html', context )


def workman_services(request):
    context = {}
    return render(request, 'webpages/workman_services.html', context )


def workman_join(request):
    context = {}
    return render(request, 'webpages/workman_services.html', context )


def realtor_services(request):
    context = {}
    return render(request, 'webpages/realtor_services.html', context )


def realtor_join(request):
    context = {}
    return render(request, 'webpages/realtor_services.html', context )


def property_services(request):
    context = {}
    return render(request, 'webpages/property_services.html', context )


def property_join(request):
    context = {}
    return render(request, 'webpages/property_services.html', context )



def careers_list(request):
    jobs = webpage_models.JobList.objects.all()
   
    context = {
               'jobs': jobs
               }
    return render(request, 'webpages/careers_list.html', context)

def careers_submit(request ,  job_id):
    
    if request.method == 'POST':
        form = CareersApplicationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.job_id = job_id
            form.save()

            messages.success(
                request, 'Form submission successful')
            return redirect('webpages:services')

        return HttpResponseRedirect(request.path_info)
    form = CareersApplicationForm()
    context = {'form': form,
              
               }
    return render(request, 'webpages/careers_submit.html', context)


def careers_add(request):
    
    if request.method == 'POST':
        form = CareersAddForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            
            form.save()

            messages.success(
                request, 'Career create successful')
            return redirect('webpages:services')

        return HttpResponseRedirect(request.path_info)
    form = CareersAddForm()
    context = {'form': form,
              
               }
    return render(request, 'webpages/careers_add.html', context)


def handler404(request, exception):
    return render(request, 'webpages/page_not_found.html', status=404)


def handler500(request):
    return render(request, 'webpages/server_error.html', status=500)



# @ login_required(login_url='/accounts/login/')
class group_memebership(ListView):
    model = webpage_models.MobSubscriber
    template_name = 'webpages/whatsapp/group_memebership.html'
    context_object_name = 'members'

    def get_context_date(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['groups'] = webpage_models.MobSubscriber.grouplist.all()

        return context


def whatsapp_group(request):
    groups = webpage_models.GroupList.objects.all()

    data = {
        'groups': groups
    }
    return render(request, 'webpages/whatsapp/whatsapp_group.html', data)


def choose_dashboard(request):
    profile = accounts_models.Profile.objects.filter(user = request.user)
    role_list = []
    
    profile = accounts_models.Profile.objects.get(user=request.user)
    print("Profile", profile)
    if profile.is_business == True:
        role_list.append("is_business")
    if profile.is_realtor == True:
        role_list.append("is_realtor")
    if profile.is_workman == True:
        role_list.append("is_workman")
    print('role_list', role_list)
    print(len(role_list))
    if len(role_list) == 0:
        print('role_list is 0')
        return redirect('accounts:profile')

    
    data = {
        'role_list' : role_list
    }
    return render(request, 'webpages/choose_dashboard.html', data)