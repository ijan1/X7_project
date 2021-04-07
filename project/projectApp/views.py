from django.shortcuts import render, redirect
from django.views.generic import View

from projectApp import forms

from django.core.files.storage import FileSystemStorage

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

    def post(self, request, *args, **kwargs):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            print("the email is " + str(email) + " and the pass is " + str(password) + " for the person " + str(name))


            return redirect('SignUp')
        return render(request, 'SignUp.html', {'form' : form})


class ForgotPass(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ForgotPass.html")

    def post(self, request, *args, **kwargs):
        form = forms.ForgotPassForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print("the email is " + str(email))

            return redirect('ForgotPass')
        return render(request, 'ForgotPass.html', {'form' : form})


'''
class styles_diana(View):
    def get(self, request, *args, **kwargs):
        return render(request, "bootstrap/css/styles_diana.css")


class bootstrapMin(View):
    def get(self, request, *args, **kwargs):
        return render(request, "bootstrap/css/bootstrap.min.css")
'''

class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AboutPage.html")


class AddItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AddItem.html")

    def post(self, request, *args, **kwargs):
        form = forms.AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            itemName = form.cleaned_data['itemName']
            category = form.cleaned_data['category']
            condition = form.cleaned_data['condition']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            print("the item " + str(itemName) + " with category " + str(category) + " and condition " + str(
                condition) + " and description " + str(description) + " and filename " + str(file))

            return redirect('AddItem')
        else:
            print("error")
        return render(request, 'AddItem.html', {'form': form})

        '''if request.FILES['file']:
            print("YES")
            print(request.FILES['file'])
            return redirect('AddItem')
        '''

class BrowseItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "BrowseItem.html")

    def post(self, request, *args, **kwargs):
        form = forms.BrowseItemForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print("you searched for " + str(search))

            return redirect('BrowseItem')
        return render(request, 'BrowseItem.html', {'form': form})


class CharityView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Charity.html")


class CartPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "CartPage.html")
    

class ItemTemplateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ItemTemplate.html")

class DecisionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Decision.html")

class DonateItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "DonateItem.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Contact.html")

    def post(self, request, *args, **kwargs):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print("the email is " + str(email) + " and the subject is " + str(subject) + " and typed the message " + str(message))

            return redirect('Contact')
        return render(request, 'Contact.html', {'form' : form})


class MapView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Map.html")

class indexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

class DonationPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "DonationPage.html")
