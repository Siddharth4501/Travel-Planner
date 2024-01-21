from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# from Travelbook.models import Contact
from Travelbook.models import Flights
from Travelbook.models import Booking
from Travelbook.models import bookeddata
from Travelbook.models import Payment
from Travelbook.models import Booking_return
import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.urls import reverse
# from travelbook.crosscheck_booking import check_booking
from Travel_Inspiration.settings import *
import razorpay
client=razorpay.Client(auth=(KEY_ID,KEY_SECRET))
from time import time
from Travelbook.models import bookeddata1

#  from travelbook.convert import json_to_object



from django.contrib.auth.decorators import login_required

# Create your views here.


def signin(request):
   return render(request,"Travel_flight_booking_template/login.html")


def mybooking(request):
   if request.user.is_staff:
      booking=Booking.objects.all()
      booking_return=Booking_return.objects.all()
   else:
      booking=Booking.objects.filter(user=request.user)
      booking_return=Booking_return.objects.filter(user=request.user)
      

   return render(request,"Travel_flight_booking_template/mybooking.html",{'booking':booking,'booking_return':booking_return})


def bookingreceipt(request):
   if request.method=='POST':
      id_of_bookingreceipt_ob=request.POST['id_of_bookingreceipt']
      booking_receipt_object=Booking.objects.get(id=id_of_bookingreceipt_ob)
      print(booking_receipt_object)
   return render(request,'Travel_flight_booking_template/bookingreceipt.html',{'booking_receipt_object':booking_receipt_object})
   
   



def handleSignup(request):
   if request.method=='POST':
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      error=None
      if (
         len(password)<8
         or not any(char.isdigit() for char in password)
         or not any(char.isupper() for char in password)
         or not any(char.islower() for char in password)
         or not any(char in '!@#$%^&*()_+' for char in password)
      ):
         error="Password does not meet the requirements, Please try again!!!"
         return render(request,'Travel_flight_booking_template/login.html',{'error':error})
      myuser=User.objects.create_user(username,email,password)
      myuser.save()
      return redirect('signin')
   else:
      return HttpResponse(" NOT FOUND")
   return render(request,'Travel_flight_booking_template/login.html')
   
def handleLogin(request):
   
   if request.method =='POST':

      loginusername=request.POST.get('loginusername')
      loginpassword=request.POST.get('loginpassword')

      user=authenticate(request,username=loginusername,password=loginpassword)
      
      if user is not None:

         login(request,user)
         #messages.success(request,"Successfully Logged In")
         return redirect('flight_user')
      else:
         return HttpResponse("user or password is incorrect")
      
   return render(request,'Travel_flight_booking_template/user.html')
   

def flight_user(request):
   flightdata=Flights.objects.all()
   
   l=[]
   z=[]
   
   for i in flightdata:
      l.append(i.From)
      z.append(i.To)
   my_list1=list(set(l))
   my_dict1={}
   my_dict2={}
   my_list2=list(set(z))
   for i in my_list1:
      my_dict1[i]=i
   for i in my_list2:
      my_dict2[i]=i
   print(my_dict1,my_dict2)
   data={
      'flightdata':flightdata,
      'dict1':my_dict1,
      'dict2':my_dict2,

   }
   

   
   return render(request,"Travel_flight_booking_template/user.html",data)
# def contact1(request):


#    if request.method=='POST':
#       #always keep different names of key in different forms eg,contact-username in contact form and username in signup
#       username=request.POST.get('contact-username')
#       email=request.POST.get('contact-email')
#       phone=request.POST.get('contact-phone')
#       message=request.POST.get('contact-message')
#       contact=Contact(username=username,email=email,phone=phone,message=message)
#       contact.save()
#       return redirect('home')
#    else:
#       return HttpResponse("something went wrong")
#    return render(request,"index.html")


def bkr(request):
   
   From=request.POST.get('from')
   To=request.POST.get('to')
   Depart_date=request.POST.get('depart-date')
   Return_date=request.POST.get('return-date')
   Class=request.POST.get('class')
   No_of_person=request.POST.get('no_of_person')
   if Return_date is not None:
      flightdata1=Flights.objects.filter(From=From,To=To,Depart_date=Depart_date,Return_date=Return_date,Class=Class)
      flightdata2=Flights.objects.filter(From=To,To=From,Depart_date=Return_date,Class=Class)
   # bookdata=Booking.objects.filter()
   else:
      flightdata1=Flights.objects.filter(From=From,To=To,Depart_date=Depart_date,Class=Class)
      flightdata2=None
   
      
         
   
     
   data={
      'flightdata1':flightdata1,
      # 'bookdata':bookdata,
      'flightdata2':flightdata2,
      'From':From,
      'To':To,
      'Depart_date':Depart_date,
      'Return_date':Return_date,
      'Class':Class,
      'No_of_person':No_of_person,
   }
   
   return render(request,'Travel_flight_booking_template/booking.html',data)


@csrf_exempt
def thanks(request):
   if request.method=='POST':
      data=request.POST
      context={}
      print(data)
      try:
         client.utility.verify_payment_signature(data)
         razorpay_order_id=data['razorpay_order_id']
         razorpay_payment_id=data['razorpay_payment_id']
         payment=Payment.objects.get(order_id=razorpay_order_id)
         payment.payment_id=razorpay_payment_id
         payment.status=True
         
         print("hello")
         if Payment.objects.filter(payment_id=razorpay_payment_id).exists():
            print("hell1")
            
         else:
            
            booking=Booking(user=payment.user,flight=payment.flight)
            booking_return=Booking_return(user=payment.user,flight1=payment.flight1)
            payment.save()
            booking.save()
            booking_return.save()
            print(booking)
         
            print(booking_return)
         
            print(payment)
            print("hell2")
         print("hello1")
         
         
         return render(request,'Travel_flight_booking_template/thanks.html',context=context)
      except:
         return HttpResponse("Invalid Payment Details")
   return render(request,'Travel_flight_booking_template/thanks.html')
   # pri1=request.POST.get('bookedfinal1')
   # bkobj=Flights.objects.get(id=pri1)
   
   # booking=Booking(user=request.user,flight=bkobj)
   # if check_booking(bkobj):
   #    pass
   # else:
   #    booking.save()
   # print(pri1)
   # dict3={
   #    'pri1':pri1,
   # }
   

def bookingreceipt(request):
   
   flightdata=Flights.objects.all()
   
      
   
   bookdata=Booking.objects.all()
      
   data={
      'flightdata':flightdata,
      'bookdata':bookdata,
      
      
      
   }
   return render(request,'Travel_flight_booking_template/bookingreceipt.html',data)

def logOUT(request):
   logout(request)
   return redirect('signin')


def bookedData(request):
   # if request.method=='POST':
   #    pri=request.POST.get('bookedfinal')
   #    print(pri)
   #    bkobj=Flights.objects.get(id=pri)
   #    dict2={
   #       'bkobj':bkobj,
   #    }
   # return redirect(reverse('payment'),data=dict2)
   return render(request,'Travel_flight_booking_template/mybooking.html')
   

def trail(request):
   if request.method=='POST':
      p=bookeddata.objects.all()
      p1=bookeddata1.objects.all()
      p.delete()
      p1.delete()
      pri=request.POST.get('bookedfinal')
      print(pri)
      pri_roundtrip=request.POST.get('bookedfinal_roundtrip')
      print(type(pri_roundtrip))
      pr=bookeddata(p=pri)
      pr.save()
      if int(pri_roundtrip)==0:
         print("hello")
         pass
      else:
         pr1=bookeddata1(p1=pri_roundtrip)
         pr1.save()
      
      p=bookeddata.objects.all()
      for i in p:
         pri3=i.p
      flight=Flights.objects.get(id=pri3)
      print(flight)
      p1=bookeddata1.objects.all()
      print(p1)
      if p1:
         for i in p1:
            pri4=i.p1
         
         flight1=Flights.objects.get(id=pri4)
         
         print(flight1)
         sum=(flight.price)+(flight1.price)+100
      else:
         flight1=None
         sum=(flight.price)+50
      
      # flight=Flights.objects.get(id=pri)
      # print(flight)
      dict2={'sum':sum,'flight':flight,'flight1':flight1}
   else:
      # p=bookeddata.objects.all()
      # for i in p:
      #    pri3=i.p
      # p1=bookeddata1.objects.all()
      # for i in p1:
      #    pri4=i.p1
      # flight=Flights.objects.get(id=pri3)
      # flight1=Flights.objects.get(id=pri4)
      # print(flight)
      # print(flight1)
      # sum=(flight.price)+(flight1.price)
      p=bookeddata.objects.all()
      for i in p:
         pri3=i.p
      flight=Flights.objects.get(id=pri3)
      print(flight)
      p1=bookeddata1.objects.all()
      print(p1)
      if p1:
         for i in p1:
            pri4=i.p1
         
         flight1=Flights.objects.get(id=pri4)
         
         print(flight1)
         sum=(flight.price)+(flight1.price)+100
      else:
         flight1=None
         sum=(flight.price)+50
      user=None
      if not request.user.is_authenticated:
         return redirect("login")
      user=request.user
      # action=request.GET.get('action')
      action="create_payment"
      print(action)
      order=None
      if action=='create_payment':
         amount=(sum)*100
         currency="INR"
         notes={
            'email':user.email,
            'name':user.username,
         }
         receipt=f"TravelTrek-{int(time())}"
         order=client.order.create({'receipt':receipt,'currency':currency,'notes':notes,'receipt':receipt,'amount':amount})
         payment=Payment()
         payment.user=user
         payment.order_id=order.get('id')
         payment.flight=flight
         if flight1:
            payment.flight1=flight1
         payment.amount=sum
         payment.save()
         print(payment)
         p1.delete()
         p.delete()
         dict2={
            'order':order,
            'user':user,
         }
         print(dict2)
         
      
         
   return render(request,'Travel_flight_booking_template/try.html',dict2)


# def payment(request):
   # data_received=request.POST.get('data',None)
   # print(data_received)
   # if(data_received):
   #    data_dict=eval(data_received)
   # else:
   #    data_dict={}
   # print(data_dict)
   # if request.method=='POST':
   #    pri=request.POST.get('bookedfinal')
   #    print(pri)
   #    bkobj=Flights.objects.get(id=pri)
   #    dict2={
   #       'bkobj':bkobj,
   #       'pri':pri,
   #    }
   # return render(request,"payment.html")


def weatherforecast(request):
   return render(request,'Travel_flight_booking_template/weatherforecast.html')