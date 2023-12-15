from django import forms
from .models import *
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineCheckboxes, StrictButton


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = MobSubscriber
        fields = ['name', 'mobile_no', 'is_agent', 'is_owner']

        widgets = {
            'btn-check': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px;'}),
        }
        labels = {
            'mobile_no': 'Mobile No: (Only Qatar Mob No, without 974)',
            'is_agent': 'Agents :: Marketing',
            'is_owner': 'I Own Property :: Re-renting',
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



class CareersApplicationForm(forms.ModelForm):
    class Meta:
        model = CareersApplication
        fields = '__all__'