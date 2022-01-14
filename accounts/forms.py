from django import forms
from django.http import request
from accounts.models import *


class AgentForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ['name', 'email', 'phone',
                  'whatsapp', 'languages', 'profile_image']
        exclude = ['user', 'roles', 'active', 'verified']
