from django import forms
from django.db import models

class LoginForm(forms.Form):
    password = forms.CharField(max_length=300)
    email = forms.EmailField(max_length=300)

class ForgotPassForm(forms.Form):
    email = forms.CharField(max_length=300)

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300)
    email = forms.EmailField(max_length=300)

class AddItemForm(forms.Form):
    itemName = forms.CharField(max_length=300)
    category = forms.CharField(max_length=300)
    condition = forms.CharField(max_length=300)
    description = forms.CharField(max_length=500)
    file = forms.FileField()

class BrowseItemForm(forms.Form):
    search = forms.CharField(max_length=300)

class ContactForm(forms.Form):
    email = forms.CharField(max_length=300)
    subject = forms.CharField(max_length=300)
    message = forms.CharField(max_length=500)
