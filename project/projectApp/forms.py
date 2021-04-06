from django import forms

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
    # file =

