from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from datetime import date
from webpages.form import ContactForm, SubscribeForm, CareersApplicationForm
from webpages import models as webpage_models
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


def services(request):
    return render(request, 'webpages/services.html')

#@todo
# add_property


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
