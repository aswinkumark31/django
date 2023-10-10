from django.shortcuts import render
from . forms import Mark_upload
from . models import *

# Create your views here.

def index(request):
    mark_up=Mark_upload()
    context={}
    if request.method=='POST':
        if 'submit' in request.POST:
            form=Mark_upload(request.POST)
            form.save()
    mark=Mark.objects.all()
    context["mark_up"]=mark_up
    context["mark"]=mark
    
    return render(request,'index.html',context)
