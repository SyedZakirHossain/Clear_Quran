from django.db import models
from django.db.models.fields import CharField,IntegerField,BooleanField
# Create your models here.


class topic(models.Model):
    t_id = models.CharField(max_length=500)
    tname=models.CharField(max_length=500)
    surano=models.IntegerField()
    suraname=models.CharField(max_length=100)
    verseno=models.CharField(max_length=200)
    verse=models.CharField(max_length=50000)

    def __str__(self) :
        return self.tname   
    
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    desc = models.TextField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = "Contacts"

