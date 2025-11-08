from django import forms
from property.models import *


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property_data
        exclude = ['user', 'date_created', 'date_updated', 'property_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Property name'}),
            'address': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Property address'}),
            'description': forms.Textarea(attrs={'class': 'modern-textarea', 'placeholder': 'Property description', 'rows': 4}),
            'property_type': forms.Select(attrs={'class': 'modern-select'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Number of bedrooms'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Number of bathrooms'}),
            'sqft': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Square feet'}),
            'photo_main': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
            'photo_1': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
            'photo_2': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
            'photo_3': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
        }


class PortionsForm(forms.ModelForm):
    class Meta:
        model = Portions
        fields = ['property_data', 'portion_type', 'furnished_type', 'furnished_extra_info', 'unit_no', 'floor_no', 'description', 'price', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3']
        exclude = ['user', 'date_created', 'date_updated', 'portion_code']
        widgets = {
            'property_data': forms.HiddenInput(),
            'portion_type': forms.Select(attrs={'class': 'modern-select'}),
            'furnished_type': forms.Select(attrs={'class': 'modern-select'}),
            'furnished_extra_info': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Furnished extra info'}),
            'unit_no': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Unit number'}),
            'floor_no': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Floor number'}),
            'description': forms.Textarea(attrs={'class': 'modern-textarea', 'placeholder': 'Portion description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Price'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Number of bedrooms'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Number of bathrooms'}),
            'sqft': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Square feet'}),
            'photo_main': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
            'photo_1': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
            'photo_2': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
            'photo_3': forms.FileInput(attrs={'class': 'modern-input', 'accept': 'image/*'}),
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
            'name': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Your full name'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Mobile number'}),
            'whatsapp_no': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'WhatsApp (974...)'}),
            'locations': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Preferred locations'}),
            'furnished_type': forms.Select(attrs={'class': 'modern-select'}),
            'property_type': forms.Select(attrs={'class': 'modern-select'}),
            'price_from': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Min price'}),
            'price_to': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Max price'}),
            'date_from': forms.DateTimeInput(attrs={'class': 'modern-input', 'type': 'datetime-local'}),
            'duration': forms.NumberInput(attrs={'class': 'modern-input', 'placeholder': 'Months'}),
            'property_type_other': forms.TextInput(attrs={'class': 'modern-input', 'placeholder': 'Specify other type'}),
            'notes': forms.Textarea(attrs={'class': 'modern-textarea', 'placeholder': 'Any additional requirements...', 'rows': 4}),
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

    
