from django.shortcuts import render, redirect
from django.views.generic import View

from projectApp import forms
from project import settings

from django.core.files.storage import FileSystemStorage

# Create your views here.

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users(name text primary key, email text, password text)')
connection.commit()

connection.close()

cart = []
donations = []

class LoginView(View):
    def __init__(self):
        global cart, donations
        cart = []
        donations = []

    def get(self, request, *args, **kwargs):
        self.__init__()
        return render(request, "Login.html")

    def post(self, request, *args, **kwargs):
        self.__init__()
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = str(form.cleaned_data['email'])
            password = str(form.cleaned_data['password'])
            print("the email is " + str(email) + " and the pass is " + str(password))

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            loginTheUser = False
            for pretenderName, pretenderEmail, pretenderPassword in users:
                if pretenderEmail == email and pretenderPassword == password:
                    loginTheUser = True

            connection.close()

            if loginTheUser:
                return redirect('Decision')

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

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            cursor.execute(f'INSERT INTO users VALUES("{name}", "{email}", "{password}")')
            connection.commit()

            connection.close()

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


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS items(name itemName primary key, category text, condition text, description text, fileName text)')
connection.commit()

connection.close()


class AddItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AddItem.html")

    def post(self, request, *args, **kwargs):
        form = forms.AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            itemName = form.cleaned_data['itemName']

            categories = ['Home', 'Bathroom', 'Living Area', 'Other']
            category = form.cleaned_data['category']
            category = int(category[-1]) - 1
            category = categories[category]

            conditions = ['3 months', '6 months', '9 months', '12 months']
            condition = form.cleaned_data['condition']
            condition = int(condition[-1]) - 1
            condition = conditions[condition]

            description = form.cleaned_data['description']
            file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            print("the item " + str(itemName) + " with category " + str(category) + " and condition " + str(
                condition) + " and description " + str(description) + " and filename " + str(file))

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            cursor.execute(f'INSERT INTO items VALUES("{itemName}", "{category}", "{condition}", "{description}", "{file.name}")')
            connection.commit()

            connection.close()

            donations.append(itemName)

            return redirect('BrowseItem')
        else:
            print("error")
        return render(request, 'AddItem.html', {'form': form})

        '''if request.FILES['file']:
            print("YES")
            print(request.FILES['file'])
            return redirect('AddItem')
        '''

class BrowseItemView(View):
    def __init__(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM items')
        self.items = cursor.fetchall()
        self.items = [(itemName, category, condition, description, str(settings.MEDIA_URL) + str(fileName)) for
                      itemName, category, condition, description, fileName in self.items]
        self.LIMIT = 5
        self.reachedLimit = False
        self.context = {'items' : self.items, 'reachedLimit' : self.reachedLimit}

        connection.close()

    def get(self, request, *args, **kwargs):
        self.__init__()
        return render(request, "BrowseItem.html", context=self.context)

    def post(self, request, *args, **kwargs):
        submitbutton = request.POST.get('cart')
        self.reachedLimit = False
        if submitbutton:
            if len(cart) == self.LIMIT:
                self.reachedLimit = True
                print("You're too greedy bro", self.reachedLimit)
            else:
                cart.append(submitbutton)
                print("item " + submitbutton + " has been added")

        form = forms.BrowseItemForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                self.items = [(itemName, category, condition, description, fileName) for itemName, category, condition, description, fileName in self.items if itemName == search]
            print("you searched for " + str(search))

        self.context = {'items': self.items, 'form': form, 'reachedLimit' : self.reachedLimit}
        return render(request, 'BrowseItem.html', context=self.context)


class CharityView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Charity.html")


class CartPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "CartPage.html", context={'items' : cart})
    
    def post(self, request, *args, **kwargs):
        global cart

        submitbutton = request.POST.get('cart')
        if submitbutton:
            toremove = 0
            for index in range(len(cart)):
                if cart[index] == submitbutton:
                    toremove = index
                    break
            cart.pop(toremove)
            print("item " + submitbutton + " has been removed")

        checkout = request.POST.get('checkout')
        if checkout:
            for item in cart:
                connection = sqlite3.connect('data.db')
                cursor = connection.cursor()

                cursor.execute(f'DELETE FROM items WHERE name="{item}"')
                connection.commit()

                connection.close()
            cart = []

        return render(request, "CartPage.html", context={'items' : cart})


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
        return render(request, "DonationPage.html", {'donations' : donations})
