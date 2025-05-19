from django import forms
from property.models import *


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building_data
        exclude = ['user', 'date_created', 'date_updated', 'building_code']


class PortionsForm(forms.ModelForm):
    class Meta:
        model = Portions
        exclude = ['user', 'building_data', 'date_created', 'date_updated', 'portion_code']

class Singelform(forms.ModelForm):
    class Meta:
        model = Portions
        fields = '__all__'
        widgets = {
            'building_data': forms.HiddenInput(),
        }

    building_name = forms.CharField(max_length=255)
    building_address = forms.CharField(max_length=255)

    def save(self, commit=True):
        building_data = Building_data(
            name=self.cleaned_data['building_name'],
            address=self.cleaned_data['building_address']
        )
        if commit:
            building_data.save()
        portion = super().save(commit=False)
        portion.building_data = building_data
        portion.building_data_id = building_data.id
        if commit:
            portion.save()
        return portion

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
        widgets = {
            'date_from': DateInput(),
        }
        labels = { 
            'date_from': 'Date From',
            'duration': 'Duration In Months',
            'locations': 'List preffered Locations'
        }

    def clean_whatsapp_no(self):
            whatsapp_no = str(self.cleaned_data.get('whatsapp_no'))
            if not (whatsapp_no.startswith('974') or whatsapp_no.startswith('+974')):
                raise forms.ValidationError("WhatsApp number must start with '974' or '+974'.")
            return whatsapp_no

    
