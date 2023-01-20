from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from datetime import date
from webpages.form import ContactForm, SubscribeForm
from webpages.models import MobSubscriber
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
            p = MobSubscriber(name=name1, mobile_no=mobile_no1,
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

        return HttpResponseRedirect(request.path_info)
    form = ContactForm()
    context = {'form': form}

    return render(request, 'webpages/contact.html', context)


def services(request):
    return render(request, 'webpages/services.html')


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


@ login_required(login_url='/accounts/login/')
def profile(request):
    pk = request.user.id
    print(pk)
    return render(request, 'webpages/profile.html')


# @ login_required(login_url='/accounts/login/')
class group_memebership(ListView):
    model = MobSubscriber
    template_name = 'webpages/whatsapp/group_memebership.html'
    context_object_name = 'members'

    def get_context_date(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['groups'] = MobSubscriber.grouplist.all()

        return context


def whatsapp_group(request):

    return render(request, 'webpages/whatsapp/whatsapp_group.html')
