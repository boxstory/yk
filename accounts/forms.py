from django import forms
from django.http import request
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML


from accounts import models as accounts_models


class AgentForm(forms.ModelForm):

    class Meta:
        model = accounts_models.Agent
        fields = ['name', 'email', 'phone',
                  'whatsapp', 'languages', 'profile_image']
        exclude = ['user', 'roles', 'active', 'verified']
        labels = {
            'phone': 'Mobile No: (Only Qatar Mob No, without 974)',
            'whatsapp': 'Whatsapp No: (Only Qatar Mob No, without 974)',
            'languages': 'Select Known Languages',
        }
        widgets = {
            'language': forms.ModelChoiceField(queryset=accounts_models.Spoken_Languages.objects.all()),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = accounts_models.Profile
        fields = '__all__'
        exclude = ['user', 'username', 'created_at', 'updated_at', 'is_staff']
        labels = {
            'is_business': ' Are you own or manage Properties',
            'is_agent': ' Are you Properties agents',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        r = accounts_models.Profile.objects.filter(email = email)
        if r.count():
            raise forms.ValidationError('Email id is already exists')
        return email
    
    

    
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = accounts_models.ProfilePicture
        fields = ['profile_picture',]


    