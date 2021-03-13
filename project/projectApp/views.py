from django.shortcuts import render, redirect
from django.views.generic import View

from projectApp import forms

# Create your views here.

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Login.html")

    def post(self, request, *args, **kwargs):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("the email is " + str(email) + " and the pass is " + str(password))
            return redirect('contact')
        return render(request, 'Login.html', {'form' : form})
