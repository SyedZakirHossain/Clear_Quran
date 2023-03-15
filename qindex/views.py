from django.shortcuts import render
from .models import img, topic

from django.shortcuts import render,redirect


from django.contrib import messages
from django.http import FileResponse
import io
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html') 

def log(request):
    return render(request,'login.html')

def tlinfo(request,topicno ):
    # topiclist=topic.objects.all()
    # tp = topic.objects.all().order_by ('topicno')
     tp = topic.objects.all()
     context = { tp: topic }

     #return render(request,'Topic_info.html',context,{'top':tp})                        
     return render(request,'Topic_info.html',context,{'top':tp})  


#def tlinfo(request,topicno ):
    # topiclist=topic.objects.get(pk=tref)
    # tp = topic.objects.all().order_by ('topicno')
    # tp = topic.objects.all()
    # context = { tp: topic }

     #return render(request,'Topic_info.html',context,{'top':tp})                        
     #return render(request,'single.html',context,{'top':tp})  
 

def qr(request):
     tp = topic.objects.filter(topicno=1001)
     context = { }
     
     return render(request,'quran.html',{'top':tp}) 

def single(request):
     context = {}  
    # topiclist=topic.objects.get(pk=tref)
     tp = topic.objects.all().order_by ('topicno')
     return render(request,'singletopic.html',{'top':tp}) 

           
def qrn(request):
   
     tp = topic.objects.all().order_by ('topicno')
     return render(request,'qrn.html',{'top':tp}) 
def pic(request):
    im = img.objects.all()
    return render(request,'pic.html',{'img':im}) 

def tl(request):
     tp = topic.objects.all().order_by ('topicno')
     return render(request,'Topic_List.html',{'top':tp}) 


 