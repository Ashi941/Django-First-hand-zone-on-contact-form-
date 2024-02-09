
#myproject/contacts/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page,name ="home-page"),
    path('contact',contact_us,name ="contact-US"),
]