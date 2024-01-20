from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import AgentForm
from accounts import models as accounts_models
# Create your views here.


@login_required(login_url='account_login')
def user_profile(request):
    profile = accounts_models.Profile.objects.get_or_create( user_id=request.user.id )
    
    data = {
        'profile' : profile
    }
    return render(request, 'accounts/user_profile.html', data)


@login_required(login_url='account_login')
def update_user_profile(request):
    profile = accounts_models.Agent.objects.filter(user_id=request.user.id)
    
    data = {
        'profile' : profile
    }
    return render(request, 'accounts/update_user_profile.html', data)


@login_required(login_url='account_login')
def agent_profile(request):
    agent = accounts_models.Agent.objects.filter(user_id=request.user.id)
    if agent:
        agent_all = accounts_models.Agent.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/agent_features.html', {'agent': agent_all})
    else:
        agent = "No Agent Profiles"
    return render(request, 'accounts/agent_features.html', {'agent': agent})



# join_marketing

@login_required(login_url='account_login')
def join_marketing(request):
    form = AgentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.roles_id = '3'

            print('join_marketing form is valid')
            form.save()
            return redirect('accounts:agent_profile', request.user.id)
        else:
            print('Form not valid')
            print(form)

    return render(request, 'accounts/join_marketing.html', {'form': form})
