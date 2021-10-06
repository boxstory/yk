from django.forms import ModelForm
from django import forms
from .models import *


class MobSubscriberForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    mobile_no = forms.CharField(
        label='Mob Number', max_length=12, min_length=1)

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(mobile_no) != 1:
            raise forms.ValidationError("Mobile Number should be 10 digits")
        return mobile_no


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = MobSubscriber
        fields = ['name', 'mobile_no']
