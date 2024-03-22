import os
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image
import random
import string

from django.contrib.auth.models import User
from accounts import forms as accounts_forms
from accounts import models as accounts_models
# Create your views here.

def unique_id(num):
        allowed_chars = ''.join((string.ascii_letters, string.digits))
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(int(num)))
        print(unique_id)
        return unique_id

@login_required(login_url='account_login')
def profile(request):
    if accounts_models.Profile.objects.filter(user=request.user).exists():
        profile = accounts_models.Profile.objects.filter( user_id=request.user.id)[0]
    else:
        profile = accounts_models.Profile.objects.create( user_id=request.user.id, first_name=request.user.first_name, last_name=request.user.last_name, username=request.user.username, email=request.user.email)

    if accounts_models.ProfilePicture.objects.filter(user=request.user).exists():
        profile_picture = accounts_models.ProfilePicture.objects.filter( user_id=request.user.id)[0]
    else: 
        profile_picture = accounts_models.ProfilePicture.objects.create( user_id=request.user.id, profile_id=request.user.profile.id)
    
    data = {
        'profile' : profile,
        'profile_picture' : profile_picture,
    }
    return render(request, 'accounts/profile.html', data)


@login_required(login_url='account_login')
def profile_update(request):
    profile = accounts_models.Profile.objects.get(user_id=request.user.id)
    form = accounts_forms.ProfileForm(instance=profile)
    if request.method == 'POST':
            print('ProgfileUpdateForm')
            form = accounts_forms.ProfileForm(
                request.POST, instance=profile)
            if form.is_valid():
                f = form.save(commit=False)
                print('f.user')

                print(f.user)

                form.save()
                print('ok')
                messages.success(request, "Successful Submission")
                return redirect("accounts:profile")
            else:
                messages.error(request, "Error")
    
    data = {
        'profile' : profile,
        'form' : form,
    }
    return render(request, 'accounts/profile_update.html', data)



def profile_picture_update(request):
    profile_picture = get_object_or_404(accounts_models.ProfilePicture, user_id=request.user.id)
    username = accounts_models.Profile.objects.get(user_id=request.user.id).username
    print(username)
    
    form_pic = accounts_forms.ProfilePictureForm()
    if request.method == 'POST':
            print('ProfilePictureForm')
            form = accounts_forms.ProfilePictureForm(
                request.POST, request.FILES, instance=profile_picture)
            if form.is_valid():
                f = form.save(commit=False)
                print('f.profile_picture')
                print(f.profile_picture)
                f.username = f'accounts/{username}'

                print('ProfilePicture filename: %s' % f)
                f.save()
                # Open the original image using Pillow
                print(f.profile_picture.path)
                original_image = Image.open(f.profile_picture.path)
                outfile = os.path.splitext(f.profile_picture.path)[0] + ".thumbnail"
                size = (128, 128)
                with Image.open(f.profile_picture.path) as im:
                    print(f.profile_picture.path, im.format, f"{im.size}x{im.mode}")
                    im.thumbnail(size)
                    im.save(outfile, "JPEG")
                print(outfile)
                title, ext = os.path.splitext(f.profile_picture.path)
                print(title, ext)
                final_filepath = os.path.join(f.profile_picture.path, title  + ext)
                print(final_filepath)
                new_width  = 200
                new_height = 200
                img = original_image.resize((new_width, new_height), Image.ANTIALIAS)
                print(img)
                img.save(final_filepath)

                messages.success(request, "Updated Profile Picture")
                return redirect("accounts:profile")

    context = {
        'form_pic': form,
    }
    return render(request, 'accounts/parts/profile_picture_update.html', context)

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
