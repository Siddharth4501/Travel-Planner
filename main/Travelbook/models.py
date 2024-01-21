from django.db import models
from django.conf import settings
# from datetime import datetime
from django.utils import timezone
# Create your models here.


class Flights(models.Model):
    flight_company=models.CharField(max_length=50)
    depart_time=models.TimeField()
    arrival_time=models.TimeField()
    # flight_start_city=models.CharField(max_length=30,default="")
    price=models.IntegerField(default=0)
    From=models.CharField(max_length=50)
    To=models.CharField(max_length=50)
    Depart_date=models.DateField()
    Return_date=models.DateField(null=True,blank=True)
    Class=models.CharField(max_length=50,default="")
    No_of_seats=models.IntegerField(default=0)
    
    
class Booking_return(models.Model):
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=False,on_delete=models.CASCADE)
    flight1=models.ForeignKey(Flights,null=True,blank=True,on_delete=models.CASCADE)
    date_of_booking=models.DateTimeField(default=timezone.now)
    # def save(self,*args,**kwargs):
    #     if Booking_return.objects.exists() and not self.pk:
    #         pass
    #     else:
    #         super(Booking_return,self).save(*args,**kwargs)
         
class Booking(models.Model):
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=False,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flights,null=False,on_delete=models.CASCADE)
    date_of_booking=models.DateTimeField(default=timezone.now)
    # def save(self,*args,**kwargs):
    #     if Booking.objects.exists() and not self.pk:
    #         pass
    #     else:
    #         super(Booking,self).save(*args,**kwargs)
    
   
# class Contact(models.Model):
#     username=models.CharField(max_length=50)
#     email=models.EmailField()
#     phone=models.IntegerField()
#     message=models.CharField(max_length=120)
    
class bookeddata(models.Model):
    p=models.IntegerField()
    def save(self,*args,**kwargs):
        if bookeddata.objects.exists() and not self.pk:
            pass
        else:
            super(bookeddata,self).save(*args,**kwargs)
        



class Payment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    order_id=models.CharField(max_length=50,null=False)
    payment_id=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    flight=models.ForeignKey(Flights,null=True,blank=True,on_delete=models.CASCADE)
    flight1=models.ForeignKey(Flights,null=True,related_name='return_bookings',on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    

class bookeddata1(models.Model):
    p1=models.IntegerField()
    def save(self,*args,**kwargs):
        if bookeddata1.objects.exists() and not self.pk:
            pass
        else:
            super(bookeddata1,self).save(*args,**kwargs)
