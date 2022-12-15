from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import AgentForm
from accounts.models import Agent
# Create your views here.


@login_required(login_url='account_login')
def agent_profile(request, pk):
    agent = Agent.objects.get(user_id=pk)
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
