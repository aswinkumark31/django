from django.shortcuts import render
from . models import *
from.forms import *

# Create your views here.
def index(request):
    enq=Enquiry.objects.all()
    form_obj=Application_Form()



    if request.method=="POST":
        if 'save' in request.POST:
            fo=Application_Form(request.POST)
            fo.save()

        elif 'delete' in request.POST:
            key=request.POST.get('delete')
            fo=Enquiry.objects.get(id=key)
            fo.delete()



    context={}

    context['enq']=enq
    context['form_obj']=form_obj
    return render(request,'index.html',context)
