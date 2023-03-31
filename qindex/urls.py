from django.urls import include,path
from . import views

app_name = "qindex"

urlpatterns = [
     
     path('', views.home, name='home'),
     path('qr', views.qr,name='qr'), 
     path('tl', views.tl,name='tl'),
     path('tl1/', views.tl1,name='tl1'),
     path('tl2/', views.tl2,name='tl2'),
     path('tl3/', views.tl3,name='tl3'),
     path('tl4/', views.tl4,name='tl4'),
     path('contact/', views.contact,name='contact'),
     path('contact/contactsave', views.contactsave, name="contactsave"),
]
