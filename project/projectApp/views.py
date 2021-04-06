from django.shortcuts import render, redirect
from django.views.generic import View

from projectApp import forms

# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Login.html")

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("the email is " + str(email) + " and the pass is " + str(password))

            return redirect('login')
        return render(request, 'Login.html', {'form' : form})


class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, "SignUp.html")


class ForgotPass(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ForgotPass.html")


class styles_diana(View):
    def get(self, request, *args, **kwargs):
        return render(request, "bootstrap/css/styles_diana.css")


class bootstrapMin(View):
    def get(self, request, *args, **kwargs):
        return render(request, " bootstrap/css/bootstrap.min.css")


class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AboutPage.html")


class AddItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AddItem.html")

    def post(self, request, *args, **kwargs):
        form = forms.AddItemForm(request.POST)
        if form.is_valid():
            itemName = form.cleaned_data['itemName']
            category = form.cleaned_data['category']
            condition = form.cleaned_data['condition']
            description = form.cleaned_data['description']
            print("the item " + str(itemName) + " with category " + str(category) + " and condition " + str(condition) + " and description " + str(description))

            return redirect('AddItem')
        return render(request, 'AddItem.html', {'form': form})