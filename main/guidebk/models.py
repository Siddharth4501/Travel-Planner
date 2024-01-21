from django.db import models 
from django.conf import settings
from datetime import datetime


# Create your models here.
class Guide(models.Model):
    guide_image=models.ImageField(upload_to='static/pictures',max_length=255)
    guide_id=models.CharField(max_length=18,primary_key=True)
    guide_name=models.CharField(max_length=50)
    guide_city=models.CharField(max_length=20)
    guide_rating=models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    guide_price=models.IntegerField(default=0)
    guide_phno=models.IntegerField(default=0000000000)
    
    def __str__(self):
        return f'{self.guide_name} with id {self.guide_id}'

class Gd_booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    guide=models.ForeignKey(Guide,on_delete=models.CASCADE,null=True,blank=True)
    bk_start_date=models.DateTimeField(default=datetime.now)
    bk_end_date=models.DateTimeField(default=datetime.now)
    guide_book_active_status=models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user} has booked {self.guide} from time {self.bk_start_date}'

class Payment_guide(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    guide_order_id=models.CharField(max_length=50,null=False)
    guide_payment_id=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    guide=models.ForeignKey(Guide,on_delete=models.CASCADE)
    guide_amount=models.IntegerField(default=0)
    status=models.BooleanField(default=False)

class Gddata(models.Model):
    gd_inst_id=models.CharField(max_length=20)
    def save(self,*args,**kwargs):
        if Gddata.objects.exists() and not self.pk:
            pass
        else:
            super(Gddata,self).save(*args,**kwargs)


class AvailabilityForm_Model(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    city=models.CharField(max_length=50)
    bk_start_date=models.DateTimeField()
    bk_end_date=models.DateTimeField()

    def save(self,*args,**kwargs):
        if AvailabilityForm_Model.objects.exists() and not self.pk:
            pass
        else:
            super(AvailabilityForm_Model,self).save(*args,**kwargs)