from django import forms
from django.http import request
from accounts.models import *


class AgentForm(forms.ModelForm):
    languages = forms.ModelMultipleChoiceField(
        queryset=Spoken_Languages.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-control form-check form-check-inline'})  #need to check later
            



    )

    class Meta:
        model = Agent
        fields = ['name', 'email', 'phone',
                  'whatsapp', 'languages', 'profile_image']
        exclude = ['user', 'roles', 'active', 'verified']
