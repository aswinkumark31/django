from django.shortcuts import render
from . models import *
from . forms import *

# Create your views here.
def index(request):
    if request.method== 'POST':
        form=Batch_filter(request.POST)
        if form.is_valid():
            bt=form.cleaned_data['batch']
            stu=Student.objects.filter(batch=bt)
        else:
            form=Batch_filter()
            stu=[]
    else:
        form=Batch_filter()
        stu=[]


    context={}
    context['stu']=stu
    context['form']=form
   



    return render(request,'about.html',context)
