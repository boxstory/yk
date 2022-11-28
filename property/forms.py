from django import forms
from property.models import *


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building_info
        exclude = ['user', 'date_created', 'date_updated']


class PortionsForm(forms.ModelForm):
    class Meta:
        model = Portions
        exclude = ['building_info', 'date_created', 'date_updated']


class InquireForm(forms.ModelForm):
    class Meta:
        model = Inquire
        exclude = ['date_created', 'date_updated']
