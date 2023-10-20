from django.shortcuts import render

from . forms import *
from . models import *

# Create your views here.

def index(request):
    todo=Todo.objects.all()
    form_obj=Todo_form()

    if request.method=="POST":
        if 'save' in request.POST:
            form=Todo_form(request.POST)
            form.save()
            form_obj=Todo_form()

        elif 'delete' in request.POST:
            key=request.POST.get('delete')
            form=Todo.objects.get(id=key)
            form.delete()

        



    context={}
    context['todo']=todo
    context['form_obj']=form_obj

    return render(request,'index.html',context)
