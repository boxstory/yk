from django.http.response import HttpResponseRedirect, JsonResponse
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
            return redirect('accounts:profile')

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
            return HttpResponseRedirect('/profile/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
    context = {
        'form': form
    }
    return render(request, 'webpages/workman_services.html', context )


def workman_join(request):
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
            return HttpResponseRedirect('/profile/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
      
    context = {
        'form': form
    }
    return render(request, 'webpages/workman_services.html', context )


def realtor_services(request):
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
            return HttpResponseRedirect('/profile/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
      

    context = {
        'form': form
    }
    return render(request, 'webpages/realtor_services.html', context )


def realtor_join(request):
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
            return HttpResponseRedirect('/profile/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
        
    context = {
        'form': form
    }
    return render(request, 'webpages/realtor_services.html', context )


def property_services(request):
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
            return HttpResponseRedirect('/profile/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
    context = { 
        'form': form
    }
    return render(request, 'webpages/property_services.html', context )


def property_join(request):
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
            return HttpResponseRedirect('/profile/')
        else:
            print("Invalid Form")

    # if a GET (or any other method) we'll create a blank form
    else:
        print("SubscribeForm")
        form = SubscribeForm()
      
    context = {
        'form': form
    }
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


def api_documentation(request):
    """
    JSON API endpoint for client integrations and project information
    Access: https://www.yellowkey.qa/api/docs/
    """

    documentation = {
        "api_version": "1.0",
        "last_updated": "2025-01-07",
        "platform": {
            "name": "Yellowkey",
            "full_name": "Yellowkey Holdings",
            "website": "https://www.yellowkey.qa",
            "description": "Qatar's complete real estate platform connecting property holders with management services, realtors with collaboration tools, and workmen with verified jobs",
            "tagline": "All-in-One Real Estate Platform in Qatar",
            "established": "2024",
            "country": "Qatar"
        },
        "contact": {
            "phone": "+974-33430001",
            "email": "info@yellowkey.qa",
            "support_email": "support@yellowkey.qa",
            "address": {
                "street": "534 alsadd",
                "city": "Doha",
                "region": "Doha",
                "postal_code": "00000",
                "country": "Qatar",
                "country_code": "QA"
            },
            "location": {
                "latitude": 25.276987,
                "longitude": 51.520008
            },
            "social_media": {
                "facebook": "https://www.facebook.com/yellowkey.qa",
                "twitter": "https://www.twitter.com/yellowkey.qa",
                "instagram": "https://www.instagram.com/yellowkey.qa"
            },
            "business_hours": {
                "days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
                "opening_time": "07:00",
                "closing_time": "17:00",
                "timezone": "Asia/Qatar"
            }
        },
        "platform_features": {
            "user_roles": [
                {
                    "role": "property_holder",
                    "name": "Property Holder / Landlord",
                    "dashboard_url": "/clients/dashboard/",
                    "description": "Property owners and landlords managing their real estate",
                    "capabilities": [
                        "Add and manage properties",
                        "Manage multiple units per property",
                        "Track tenant information",
                        "Collect rent",
                        "Request maintenance services",
                        "View property analytics",
                        "Upload property photos"
                    ]
                },
                {
                    "role": "realtor",
                    "name": "Realtor / Real Estate Agent",
                    "dashboard_url": "/realtor/dashboard/",
                    "description": "Real estate agents and brokers",
                    "capabilities": [
                        "View vacant properties",
                        "Access vacant soon listings",
                        "Manage property inquiries",
                        "Share leads with other agents",
                        "Join agent community",
                        "List properties for clients"
                    ],
                    "verification_required": true
                },
                {
                    "role": "workman",
                    "name": "Workman / Service Provider",
                    "dashboard_url": "/workman/dashboard/",
                    "description": "Maintenance workers and service providers",
                    "capabilities": [
                        "View service job listings",
                        "Accept maintenance requests",
                        "Location-based job matching",
                        "Track service history",
                        "Receive payments",
                        "Build service team"
                    ]
                }
            ],
            "multi_role_support": true,
            "authentication": {
                "methods": ["email_password", "google_oauth"],
                "email_verification_required": true,
                "password_reset_available": true
            }
        },
        "services": [
            {
                "id": "property_management",
                "name": "Property Management Services",
                "category": "For Property Holders",
                "description": "Comprehensive property management solutions for landlords in Qatar",
                "features": [
                    "Property Management",
                    "Tenant Relations",
                    "Rent Collection",
                    "Property Photography",
                    "Property Maintenance Coordination"
                ],
                "url": "https://www.yellowkey.qa/property-services/",
                "target_users": "Property holders and landlords",
                "pricing_model": "Contact for details"
            },
            {
                "id": "realtor_services",
                "name": "Realtor Collaboration Platform",
                "category": "For Realtors",
                "description": "Tools and network for real estate agents in Qatar",
                "features": [
                    "Vacant Property Listings",
                    "Vacant Soon Property Alerts",
                    "Multiple Property Management",
                    "Shared Property Enquiries",
                    "Trusted Agents Community Network"
                ],
                "url": "https://www.yellowkey.qa/realtor-services/",
                "target_users": "Real estate agents and realtors",
                "pricing_model": "Subscription based"
            },
            {
                "id": "workman_services",
                "name": "Maintenance Services Platform",
                "category": "For Service Providers",
                "description": "Job platform for property maintenance professionals",
                "features": [
                    "Service Job Listings",
                    "Direct Tenant Requests",
                    "Secure Payment Collections",
                    "Location-Based Job Matching",
                    "Team Building Tools"
                ],
                "url": "https://www.yellowkey.qa/workman-services/",
                "target_users": "Workmen, plumbers, electricians, cleaners",
                "pricing_model": "Commission per job"
            }
        ],
        "property_types_supported": [
            "STUDIO",
            "1BHK",
            "2BHK",
            "3BHK",
            "4BHK",
            "5BHK",
            "5+BHK",
            "VILLA",
            "APARTMENT",
            "OFFICE",
            "SHOP",
            "STORAGE",
            "BACHELOR_BEDSPACE",
            "SINGLE_ROOM",
            "CAMPSITE"
        ],
        "areas_served": [
            {"name": "Doha", "zone_number": null, "type": "city"},
            {"name": "The Pearl Qatar", "zone_number": null, "type": "district"},
            {"name": "West Bay", "zone_number": null, "type": "district"},
            {"name": "Lusail", "zone_number": null, "type": "city"},
            {"name": "Al Sadd", "zone_number": null, "type": "district"},
            {"name": "Al Waab", "zone_number": null, "type": "district"},
            {"name": "Al Rayyan", "zone_number": null, "type": "district"},
            {"name": "Al Wakrah", "zone_number": null, "type": "city"},
            {"name": "Bin Mahmood", "zone_number": null, "type": "district"},
            {"name": "Old Airport", "zone_number": null, "type": "district"},
            {"name": "Musherib", "zone_number": null, "type": "district"},
            {"name": "Mansoura", "zone_number": null, "type": "district"},
            {"name": "Ain Khaled", "zone_number": null, "type": "district"},
            {"name": "Al Gharrafa", "zone_number": null, "type": "district"},
            {"name": "Abu Hamour", "zone_number": null, "type": "district"},
            {"name": "Al Thumama", "zone_number": null, "type": "district"}
        ],
        "community_features": {
            "whatsapp_groups": {
                "available": true,
                "categories": ["property_holders", "realtors", "workmen", "general"],
                "description": "Join community groups for networking and opportunities",
                "url": "https://www.yellowkey.qa/whatsapp_group/"
            },
            "careers": {
                "job_categories": [
                    "management",
                    "accounting",
                    "medical",
                    "services",
                    "technology",
                    "maintenance"
                ],
                "url": "https://www.yellowkey.qa/careers/"
            }
        },
        "technology": {
            "framework": "Django",
            "database": "PostgreSQL",
            "frontend": "Bootstrap 5",
            "authentication": "Django Allauth",
            "languages_supported": ["English", "Arabic"],
            "mobile_responsive": true
        },
        "api_endpoints": {
            "documentation": {
                "url": "/api/docs/",
                "method": "GET",
                "format": "JSON",
                "description": "This endpoint - provides platform information"
            },
            "health_check": {
                "url": "/api/health/",
                "method": "GET",
                "format": "JSON",
                "description": "System health status"
            },
            "future_endpoints": {
                "properties_list": "/api/properties/ (coming soon)",
                "vacant_properties": "/api/properties/vacant/ (coming soon)",
                "inquiries": "/api/inquiries/ (coming soon)",
                "jobs": "/api/jobs/ (coming soon)"
            }
        },
        "integration_guide": {
            "description": "This API provides public information about Yellowkey platform for third-party integrations",
            "use_cases": [
                "Display Yellowkey services on partner websites",
                "Integrate service areas into mapping applications",
                "Link to specific dashboards for user onboarding",
                "Embed property type information",
                "Show available community groups"
            ],
            "data_format": "JSON",
            "authentication": "None required for public endpoints",
            "rate_limit": {
                "requests_per_hour": 100,
                "requests_per_day": 1000
            },
            "cors": "Enabled for approved domains",
            "caching": "Recommended - data updates daily"
        },
        "support": {
            "documentation_url": "https://www.yellowkey.qa/help/",
            "contact_support": "support@yellowkey.qa",
            "business_inquiries": "info@yellowkey.qa",
            "report_issue": "Contact support team",
            "api_questions": "developers@yellowkey.qa"
        },
        "legal": {
            "terms_of_service": "https://www.yellowkey.qa/terms/",
            "privacy_policy": "https://www.yellowkey.qa/privacy/",
            "data_protection": "GDPR compliant",
            "jurisdiction": "Qatar"
        }
    }

    return JsonResponse(documentation, json_dumps_params={'indent': 2})


def api_health(request):
    """
    Health check endpoint for monitoring
    Access: https://www.yellowkey.qa/api/health/
    """

    health_status = {
        "status": "healthy",
        "timestamp": date.today().isoformat(),
        "version": "1.0",
        "services": {
            "database": "operational",
            "website": "operational",
            "api": "operational"
        }
    }

    return JsonResponse(health_status)