from django import forms
from property.models import *


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property_data
        exclude = ['user', 'date_created', 'date_updated', 'property_code']


class PortionsForm(forms.ModelForm):
    class Meta:
        model = Portions
        fields = ['property_data', 'portion_type', 'furnished_type', 'furnished_extra_info', 'unit_no', 'floor_no', 'description', 'price', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3']
        exclude = ['user', 'date_created', 'date_updated', 'portion_code']
        widgets = {
            'property_data': forms.HiddenInput(),
        }

class Singelform(forms.ModelForm):
    class Meta:
        model = Portions
        fields = '__all__'
        widgets = {
            'property_data': forms.HiddenInput(),
        }

    property_name = forms.CharField(max_length=255)
    property_address = forms.CharField(max_length=255)

    def save(self, commit=True):
        property_data = Property_data(
            name=self.cleaned_data['property_name'],
            address=self.cleaned_data['property_address']
        )
        if commit:
            property_data.save()
        portion = super().save(commit=False)
        portion.property_data = property_data
        portion.property_data_id = property_data.id
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

    
