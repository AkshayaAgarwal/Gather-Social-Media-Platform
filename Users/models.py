from django.db import models

class Users_table(models.Model):
  username = models.CharField(max_length=255,unique=True)
  email = models.CharField(max_length=255,unique=True,null=False,primary_key=True)
  password=models.CharField(max_length=255,null=False)
  college = models.CharField(max_length=255)
  course = models.CharField(max_length=255)
  date = models.DateField()
  gender = models.CharField(max_length=255) 
  images = models.ImageField(upload_to='images',null=False)
  phone = models.CharField(max_length=15,unique=True)



  



