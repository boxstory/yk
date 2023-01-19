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



class DateInput(forms.DateInput):
    input_type = 'date'

class PortionsStatusForm(forms.ModelForm):
    class Meta:
        model = Portions_status
        exclude = ['portions']

        widgets = {
            'vacant_date': DateInput(),
        }


class InquireForm(forms.ModelForm):
    class Meta:
        model = Inquire
        exclude = ['date_created', 'date_updated']
