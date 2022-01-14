from django import forms
from property.models import *


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['user', 'date_created', 'date_updated']
