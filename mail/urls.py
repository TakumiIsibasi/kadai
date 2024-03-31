from django.urls import path
from . import views

app_name = 'emailsendapp'

urlpatterns = [
    path("", views.mail, name="mail"),
    path("contact/", views.contact, name="contact"),
]
