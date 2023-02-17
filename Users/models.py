from django.db import models

class Myuser(models.Model):
  username = models.CharField(max_length=255,unique=True)
  email = models.CharField(max_length=255,primary_key=True)
  password=models.CharField(max_length=255)
class Userinfo(models.Model):
  email = models.CharField(max_length=255)
  college = models.CharField(max_length=255)
  course = models.CharField(max_length=255)
  date = models.DateField()
  gender = models.CharField(max_length=255)

  



