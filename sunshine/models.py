
from django.db import models

# Create your models here.
class Home1(models.Model):
    objects = all('Home1')
    msg_id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="sunshine/images")

class Home2(models.Model):
    objects = all('Home2')
    msg_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,default="")
    desc=models.TextField()
    image=models.ImageField(upload_to="sunshine/images",default="")

    def __str__(self):
        return self.title




class Contact(models.Model):
    msg_id=models.AutoField(primary_key= True )
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=100,default="")
    message=models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name
