from django import forms
from django.http import request
from accounts.models import *


class AgentForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ['name', 'email', 'phone',
                  'whatsapp', 'languages', 'profile_image']
        exclude = ['user', 'roles', 'active', 'verified']
        labels = {
            'phone': 'Mobile No: (Only Qatar Mob No, without 974)',
            'whatsapp': 'Whatsapp No: (Only Qatar Mob No, without 974)',
            'languages': 'Select Known Languages',
        }
        widgets = {
            'language': forms.ModelChoiceField(queryset=Spoken_Languages.objects.all()),
        }
