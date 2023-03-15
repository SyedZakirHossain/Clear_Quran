from django.db import models
from django.db.models.fields import CharField,IntegerField,BooleanField
# Create your models here.
class topic(models.Model):

    topicno=models.IntegerField()
    tname=models.CharField(max_length=500)
    tref=models.IntegerField()
    surano=models.IntegerField()
    suraname=models.CharField(max_length=100)
    versesno=models.CharField(max_length=200)
    verse=models.CharField(max_length=50000)

    def __str__(self) :
        return self.tname
    
class img(models.Model):

    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="static/pics",default="")
    description=models.CharField(max_length=50000)
    
    def __str__(self) :
        return self.name,self.description,self.img
