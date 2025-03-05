from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
@login_required(login_url='account_login')
def dashboard(request):
    if request.user.profile.is_workman == False:
        messages.error(request, 'You are not authorized to access Wrokman Dashboard.')
        return redirect('account_login')
    profile = request.user.profile


    data = {
        'profile': profile
    }

    return render(request, 'workman/dashboard.html', data)