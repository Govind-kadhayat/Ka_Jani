from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
     return render(request,'about.html')


def services(request):
   return render(request,'services.html')

def contact(request):
      if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         address= request.POST.get('address')
         desc = request.POST.get('desc')
         # Contact = contact(name=name,email=email,address=address,phone=phone,desc=desc,date =datetime.today())
         new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            address=address,
            desc=desc,
            date=datetime.now()  # Use datetime.now() for current date and time
        )
         new_contact.save()
  
      return render(request,'contact.html')


def dashboard(request):
   return render(request,'dashboard.html')