from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def help_view(request):
    return render(request, 'help/help.html')

@login_required
def workman_help(request):
    """
    Help page for Service Providers (Workman)
    Accessible only from dashboard when logged in
    """
    context = {
        'page_title': 'Service Provider Help',
        'user_role': 'Service Provider'
    }
    return render(request, 'help/workman_help.html', context)

@login_required
def realtor_help(request):
    """
    Help page for Agents (Realtor)
    Accessible only from dashboard when logged in
    """
    context = {
        'page_title': 'Agent Help',
        'user_role': 'Agent'
    }
    return render(request, 'help/realtor_help.html', context)

@login_required
def client_help(request):
    """
    Help page for Property Owners (Clients)
    Accessible only from dashboard when logged in
    """
    context = {
        'page_title': 'Property Owner Help',
        'user_role': 'Property Owner'
    }
    return render(request, 'help/client_help.html', context)
