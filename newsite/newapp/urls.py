from django.urls import path
from . import views

urlpatterns = [
    path('',views.sample,name="sample"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact")
]
