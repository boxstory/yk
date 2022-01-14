from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from webpages.form import MobSubscriberForm, SubscribeForm
from webpages.models import MobSubscriber

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        pk = request.user.id
        print(pk)
        template = f'webpages/services.html'
        print(template)
        return render(request, template, {'pk': pk})
    else:
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
                                  date_subscribed=datetime.now, messages_received=0)
                p.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/profile/')
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

    return render(request, 'webpages/contact.html')


def services(request):
    return render(request, 'webpages/services.html')


# add_property


def add_property(request):
    return render(request, 'webpages/add_property.html')


def about(request):
    return render(request, 'webpages/about.html')


@ login_required(login_url='/accounts/login/')
def profile(request):
    pk = request.user.id
    print(pk)
    return render(request, 'webpages/profile.html')
