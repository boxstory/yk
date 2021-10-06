from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .form import MobSubscriberForm, SubscribeForm
from .models import MobSubscriber

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
                              date_subscribed=datetime.now(), messages_received=0)
            p.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("GET")
        form = SubscribeForm()

    # context = {'form': form}
    return render(request, 'webpages/home.html', {'form': form})
    # return render(request, 'webpages/home.html')


def contact(request):
    return render(request, 'webpages/contact.html')


def services(request):
    return render(request, 'webpages/services.html')


def about(request):
    return render(request, 'webpages/about.html')


@ login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'webpages/profile.html')


# def get_mob_no(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = MobSubscriberForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             name = form.cleaned_data['name']
#             print(name)
#             mobile_no = form.cleaned_data['mobile_no']
#             print(mobile_no)
#             MobSubscriber = MobSubscriberForm(name=name, mobile_no=mobile_no,
#                                               date_subscribed=datetime.now(), messages_received=0)
#             MobSubscriber.save()

#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = MobSubscriberForm()

#     return render(request, 'home', {'form': form})
