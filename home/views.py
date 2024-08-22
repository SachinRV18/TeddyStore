from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
context = {
    "variable1": "this is done by Sachin",
    "variable2": "sachin is learning Django"
}

def index(request):
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html', context)
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html', context)
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent!")
    return render(request, 'contact.html', context)
    # return HttpResponse("This is contact page")