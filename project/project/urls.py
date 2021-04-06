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

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("login", views.LoginView.as_view(), name = 'login'),
    path("styles_diana", views.styles_diana.as_view(), name = 'styles_diana'),
    path("bootstrapMin", views.bootstrapMin.as_view(), name = 'bootstrapMin'),
    path("ForgotPass", views.ForgotPass.as_view(), name = 'ForgotPass'),
    path("SignUp", views.SignUp.as_view(), name = 'SignUp'),

    path("AddItem", views.AddItemView.as_view(), name = 'AddItem'),
    path("AboutPage", views.AboutPageView.as_view(), name = 'AboutPage'),

]
