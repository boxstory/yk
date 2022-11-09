from django import forms
from django.http import request
from accounts.models import *


class AgentForm(forms.ModelForm):
    languages = forms.ModelChoiceField(
        queryset=Spoken_Languages.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-control form-check form-check-inline'})  # @todo: need to check later




    )

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
