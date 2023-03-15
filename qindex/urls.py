from django.urls import include,path
from . import views
urlpatterns = [
     
     path('', views.home, name='home'),
    
     path('qr', views.qr,name='qr'), 
     path('qrn', views.qrn,name='qrn'),
     path('tl', views.tl,name='tl'),
     path('pic', views.pic,name='pic'),
      path('tlinfo', views.tlinfo,name='tlinfo'),
     #path('tlinfo/int<tref>', views.tlinfo,name='tlinfo'),
     path('tlinfo/int<tref>', views.single,name='single'),
]
