from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'realtor/dashboard.html')

@login_required
def near_properties(request):
    return render(request, 'realtor/near_properties.html')

@login_required
def vacant_portions(request):
    return render(request, 'realtor/vacant_portions.html')

@login_required
def vacant_soon(request):
    return render(request, 'realtor/vacant_soon.html')

@login_required
def vacants(request):
    return render(request, 'realtor/vacants.html')

@login_required
def booked_properties(request):
    return render(request, 'realtor/booked_properties.html')

@login_required
def inquiries(request):
    return render(request, 'realtor/inquiries.html')

@login_required
def tenant_calls(request):
    return render(request, 'realtor/tenant_calls.html')

@login_required
def visit_requests(request):
    return render(request, 'realtor/visit_requests.html')

@login_required
def followups(request):
    return render(request, 'realtor/followups.html')

@login_required
def tenant_docs(request):
    return render(request, 'realtor/tenant_docs.html')

@login_required
def deals_reports(request):
    return render(request, 'realtor/deals_reports.html')

@login_required
def pending_requests(request):
    return render(request, 'realtor/pending_requests.html')

@login_required
def reports(request):
    return render(request, 'realtor/reports.html')

@login_required
def contacts(request):
    return render(request, 'realtor/contacts.html')

@login_required
def services_list(request):
    return render(request, 'realtor/services_list.html')

@login_required
def dashboard(request):
    return render(request, 'realtor/dashboard.html')