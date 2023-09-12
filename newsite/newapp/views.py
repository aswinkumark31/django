from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'sample.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
