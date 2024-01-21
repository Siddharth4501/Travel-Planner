from django.db import models

# Create your models here.
class Inspiration(models.Model):
    frt_pg_title=models.CharField(max_length=20,null=False)
    frt_pg_content=models.CharField(max_length=100)
    information_img=models.ImageField(upload_to='static/pictures',max_length=255)
    information_content=models.CharField(max_length=1000)

class Contact(models.Model):
    contact_info_name=models.CharField(max_length=50,null=False,blank=False) 
    contact_info_email=models.EmailField()
    contact_info_message=models.CharField(max_length=250)

class Feedback(models.Model):
    feedback_username=models.CharField(max_length=50,null=False,blank=False) 
    feedback_userimg=models.ImageField(upload_to='static/pictures',max_length=255,null=True,blank=True)
    feedback_rating=models.IntegerField(default=1)
    feedback_message=models.CharField(max_length=250)