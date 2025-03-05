from django import forms
from django.http import request
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML


from accounts import models as accounts_models


class AgentForm(forms.ModelForm):

    class Meta:
        model = accounts_models.Agent
        fields = ['agent_name', 'marketing_name',  'email', 'phone',
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
            'is_business': 'Do you own or manage Properties',
            'is_realtor': 'Are you Realtor / Properties Agents',
            'is_workman': 'Service Provider to Home or Office',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_email = self.instance.email if self.instance else None
        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['whatsapp'].widget.attrs.update({'placeholder': 'Enter mobile number without 974'})

    def clean_whatsapp(self):
        whatsapp = str(self.cleaned_data.get('whatsapp', ''))
        phone = str(self.cleaned_data.get('phone', ''))
        
        if not whatsapp and phone:
            whatsapp = phone
        
        if whatsapp and not whatsapp.startswith('974'):
            whatsapp = '974' + whatsapp
        
        
        return whatsapp
    
    print(type(clean_whatsapp))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        # Check if the email is already in use by a different profile
        existing_profile = accounts_models.Profile.objects.exclude(email=self.original_email).filter(email=email).first()

        if existing_profile:
            raise forms.ValidationError('This email address is already in use by another profile. Please use a different one.')

        return email
    
    

    
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = accounts_models.ProfilePicture
        fields = ['profile_picture',]


    