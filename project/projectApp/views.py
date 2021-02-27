from django.shortcuts import render, redirect
from django.views.generic import View

from projectApp import forms

# Create your views here.

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Login.html")

    def post(self, request, *args, **kwargs):
        form = forms.ContactForm(request.POST)
        print(form)
        if form.is_valid():
            return redirect('contact')
        return render(request, 'Login.html', {'form' : form})
