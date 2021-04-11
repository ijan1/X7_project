"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from . import index

from projectApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.indexView.as_view(), name = 'index'),
    path("index", views.indexView.as_view(), name = 'index'),
    path("login", views.LoginView.as_view(), name = 'login'),
    #path("styles_diana", views.styles_diana.as_view(), name = 'styles_diana'),
    #path("bootstrapMin", views.bootstrapMin.as_view(), name = 'bootstrapMin'),
    path("ForgotPass", views.ForgotPass.as_view(), name = 'ForgotPass'),
    path("SignUp", views.SignUp.as_view(), name = 'SignUp'),

    path("AddItem", views.AddItemView.as_view(), name = 'AddItem'),
    path("BrowseItem", views.BrowseItemView.as_view(), name = 'BrowseItem'),
    path("Charity", views.CharityView.as_view(), name = 'Charity'),
    path("CartPage", views.CartPageView.as_view(), name = 'CartPage'),
    path("ItemTemplate", views.ItemTemplateView.as_view(), name = 'ItemTemplate'),
    path("AboutPage", views.AboutPageView.as_view(), name = 'AboutPage'),
    path("DonateItem", views.DonateItemView.as_view(), name = 'DonateItem'),
    path("Decision", views.DecisionView.as_view(), name = 'Decision'),
    path("Contact", views.ContactView.as_view(), name = 'Contact'),
    path("Map", views.MapView.as_view(), name = 'Map'),
    path("DonationPage", views.DonationPageView.as_view(), name = 'DonationPage'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
