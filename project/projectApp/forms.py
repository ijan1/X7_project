from django import forms

class LoginForm(forms.Form):
    password = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
