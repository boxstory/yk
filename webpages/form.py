from django import forms
from .models import *
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineCheckboxes, StrictButton


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = MobSubscriber
        fields = ['name', 'mobile_no', 'is_realator', 'is_clients', 'is_workman']

        widgets = {
            'btn-check': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px;'}),
        }
        labels = {
            'mobile_no': 'Mobile No: (Only Qatar Mob No, without 974)',
            'is_clients': 'PROPERTIES :: Holding Properties for rental or sale',
            'is_realator': 'REALTOR :: Property Marketer',
            'is_workman': 'WORKMAN :: Mainanace service Provider for Homes and Offices',
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CareersAddForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = '__all__'



class CareersApplicationForm(forms.ModelForm):
    class Meta:
        model = CareersApplication
        fields = '__all__'