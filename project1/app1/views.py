from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    d= {
        'data':pro.objects.all()
        }
    return render(request,'about.html',d)
def contact(request):
    return render(request,'contact.html')
