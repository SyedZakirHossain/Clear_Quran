from django.shortcuts import render
from .models import  topic,Contact

from django.shortcuts import render,redirect


from django.contrib import messages
from django.http import FileResponse
import io
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html') 

def contact(request):
    return render(request,'contact.html') 
#========================================================= 
#@login_required(login_url="/login")
def contact(request):
    return render(request, "contact.html")
#========================================================= 

#@login_required(login_url="/login")
def contactsave(request):
    try:
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            desc = request.POST["desc"]
            values = Contact(name=name, email=email, desc=desc)
            values.save()
            messages.info(request, "Your message is saved and added to database. ")
            messages.info(request, "")
    except:
        pass
    return redirect("/contact")

#========================================================= 
def log(request):
    return render(request,'login.html')

def qr(request):
     tp = topic.objects.all().order_by('tname')
     context = { }
     return render(request,'quran.html',{'top':tp}) 
      

def tl(request):
     tp = topic.objects.all()
     return render(request,'Topic_List.html',{'top':tp}) 

def tl1(request):
     tp = topic.objects.all().filter(tname='Abraham')
     return render(request,'tl1.html',{'top':tp}) 

def tl2(request):
     tp = topic.objects.all().filter(tname='Lahab')
     return render(request,'tl1.html',{'top':tp}) 

def tl3(request):
     tp = topic.objects.all().filter(tname='Ahad')
     return render(request,'tl1.html',{'top':tp}) 

def tl4(request):
     tp = topic.objects.all().filter(tname='Indecencies')
     return render(request,'tl1.html',{'top':tp}) 






 