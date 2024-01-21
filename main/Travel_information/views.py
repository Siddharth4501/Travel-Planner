from django.shortcuts import render,HttpResponse,redirect
from Travel_information.models import Inspiration,Contact,Feedback
from django.contrib.auth.models import User

# Create your views here.
def home(request):
   feedback=Feedback.objects.all()
   
   return render(request,'Travel_information_template/index.html',{'feedback':feedback})

def about(request):
   return render(request,'Travel_information_template/about.html')

def feedback(request):
   if request.method=='POST':
      feedback_rating=request.POST.get('feedback_rating')
      feedback_message=request.POST.get('feedback_message')
      feedback_username=request.user
      feedback=Feedback(feedback_username=feedback_username,feedback_rating=feedback_rating,feedback_message=feedback_message)
      feedback.save()
   return render(request,'Travel_information_template/feedback.html')

def contact(request):
   if request.method=='POST':
      contact_info_name=request.POST.get('contact_name')
      contact_info_email=request.POST.get('contact_email')
      contact_info_message=request.POST.get('contact_message')
      contact=Contact(contact_info_name=contact_info_name,contact_info_email=contact_info_email,contact_info_message=contact_info_message)
      contact.save()
   return render(request,'Travel_information_template/index.html')

def user(request):
   if request.method=='POST':
      var1=request.POST.get('placesearch-box')
      inspi1=Inspiration.objects.filter(frt_pg_title=var1)
      a=True
      title=None
      firstpg_content=None
      if inspi1:
         title=var1
      for i in inspi1:
         firstpg_content=i.frt_pg_content
      dict1={'inspi1':inspi1,'a':a,'title':title,'firstpg_content':firstpg_content}
   else:
      a=False
      dict1={'a':a}
   return render(request,'Travel_information_template/user.html',dict1)


