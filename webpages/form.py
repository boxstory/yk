from django import forms


class subscriberForm(forms.Form):
    mobile_no = forms.CharField(max_length=100)
