from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("Please enter your e-mail address!")
        return email

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if len(subject) < 3:
            raise forms.ValidationError("Not enough words!")
        return subject
