from django import forms

class ContactForm(forms.Form):
    password = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
