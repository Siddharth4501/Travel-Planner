from django.shortcuts import render,HttpResponse
# from django.views.generic import FormView
from .models import Guide,Gd_booking,Payment_guide,Gddata,AvailabilityForm_Model
from .forms import AvailabilityForm
from datetime import datetime
from django.utils import  timezone
from guidebk.booking_functions.availability import check_availability
from Travel_Inspiration.settings import *
from django.views.decorators.csrf import csrf_exempt
import razorpay
client=razorpay.Client(auth=(KEY_ID,KEY_SECRET))
from time import time
# Create your views here.

def BookingView(request):
    if request.method=='POST':
        availabilityform_model=AvailabilityForm_Model.objects.all()
        if availabilityform_model:
            availabilityform_model.delete()
        # user=request.user
        # gd=request.POST.get('bookguide')
        # print("hello",gd)
        # action="create_guidepayment"
        # if gd:
        #     guide_listitem=Guide.objects.get(guide_id=gd)
        #     print("hell",gd)
        #     print(guide_listitem)
        #     order=None
        #     if action=='create_guidepayment':
        #         sum=guide_listitem.guide_price
        #         amount=(sum)*100
        #         currency="INR"
        #         notes={
        #             'email':user.email,
        #             'name':user.username,
        #         }
        #         receipt=f"TravelTrek-{int(time())}"
        #         order=client.order.create({'receipt':receipt,'currency':currency,'notes':notes,'receipt':receipt,'amount':amount})
        #         payment_guide=Payment_guide()
        #         payment_guide.user=user
        #         payment_guide.guide_order_id=order.get('id')    
        #         payment_guide.guide_amount=sum
        #         payment_guide.guide=guide_listitem
        #         payment_guide.save()
        #         print(payment_guide)
                
        #         dict5={
        #             'order':order,
        #             'user':user,
        #         }
        #         print(dict5)   
        
        
        form=AvailabilityForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            # data['bk_start_date']=data['bk_start_date'].isoformat()
            # data['bk_end_date']=data['bk_end_date'].isoformat()
            # request.session['form_data']=data
            availabilityform_model=AvailabilityForm_Model(user=request.user,city=data['city'],bk_start_date=data['bk_start_date'],bk_end_date=data['bk_end_date'])
            availabilityform_model.save()
            
        print(data)
        guide_list=Guide.objects.filter(guide_city=data['city'])
        print(guide_list)
        # action=request.GET.get('action')
        available_guides=[]
        for guide in guide_list:
            if(check_availability(guide,data['bk_start_date'],data['bk_end_date'])):
                available_guides.append(guide)
        print(available_guides)
        if len(available_guides)>0:
            # gd_booking=Gd_booking(user=request.user,bk_start_date=data['bk_start_date'],bk_end_date=data['bk_end_date'])
            # gd_booking.save()
            # if gd_booking:
            #     dictof_bookedguide={'gd_booking':gd_booking,}
            #     redirect('gdbooked',dictof_bookedguide)
            Tv=True
            dict5={
                'Tv':Tv,
                'av':available_guides,
                'form':form,
                
            }
            print(dict5)
            for n in available_guides:
                print(n)
            
        else:
            Tv=None
            a="No guides Available"
            dict5={
                'Tv':Tv,
                'a':a,
                'form':form,
            }
        # if action=='guides_detail':
        #     for guide in guide_list:
        #         if(check_availability(guide,data['bk_start_date'],data['bk_end_date'])):
        #             available_guides.append(guide)
        # print(available_guides)
        # dict5={
        #     'available_guides':available_guides,
        #     'form':form,
        # }
    else:
        form=AvailabilityForm()
        Tv=None
        dict5={
            'Tv':Tv,
            'form':form,
        }    
    return render(request,'Travel_guide_booking_template/guide_book.html',dict5)

def guidepayment(request):
    if request.method=='POST':
        gd_id_list=Gddata.objects.all()
        gd_id_list.delete()
        user=request.user
        gd=request.POST.get('bookguide')
        print("hello",gd)
        gddata=Gddata(gd_inst_id=gd)
        gddata.save()
        for i in gd_id_list:
            gd_only_item=i.gd_inst_id
        guide_listitem=Guide.objects.get(guide_id=gd_only_item)
        availabilityform_model=AvailabilityForm_Model.objects.all()
        for i in availabilityform_model:
            availabilityform_model_bk_start_date=i.bk_start_date
            availabilityform_model_bk_end_date=i.bk_end_date
        # availabilityform_model_bk_start_date=str(availabilityform_model_bk_start_date)
        # availabilityform_model_bk_end_date=str(availabilityform_model_bk_end_date)
        # booking_start_date=datetime.strptime(availabilityform_model_bk_start_date,'%Y-%m-%d')
        # booking_end_date=datetime.strptime(availabilityform_model_bk_end_date,'%Y-%m-%d')
        delta=availabilityform_model_bk_end_date-availabilityform_model_bk_start_date
        num_days=delta.days
        if num_days<1:
            sum=guide_listitem.guide_price
        else:
            sum=(guide_listitem.guide_price)*num_days
        dict_guide={
            'sum':sum,
            'guide_listitem':guide_listitem
        }
    else:
        user=request.user
        gd_id_list=Gddata.objects.all()
        for i in gd_id_list:
            gd_only_item=i.gd_inst_id
        
        action="create_guidepayment"
        if gd_only_item:
            guide_listitem=Guide.objects.get(guide_id=gd_only_item)
            print("hell",gd_only_item)
            print(guide_listitem)
            order=None
            if action=='create_guidepayment':
                availabilityform_model=AvailabilityForm_Model.objects.all()
                for i in availabilityform_model:
                    availabilityform_model_bk_start_date=i.bk_start_date
                    availabilityform_model_bk_end_date=i.bk_end_date
                # availabilityform_model_bk_start_date=str(availabilityform_model_bk_start_date)
                # availabilityform_model_bk_end_date=str(availabilityform_model_bk_end_date)
                # booking_start_date=datetime.strptime(availabilityform_model_bk_start_date,'%Y-%m-%d')
                # booking_end_date=datetime.strptime(availabilityform_model_bk_end_date,'%Y-%m-%d')
                delta=availabilityform_model_bk_end_date-availabilityform_model_bk_start_date
                
                num_days=delta.days
                if num_days<1:
                    sum=guide_listitem.guide_price
                else:
                    sum=(guide_listitem.guide_price)*num_days
                amount=(sum)*100
                currency="INR"
                notes={
                    'email':user.email,
                    'name':user.username,
                }
                receipt=f"TravelTrek-{int(time())}"
                order=client.order.create({'receipt':receipt,'currency':currency,'notes':notes,'receipt':receipt,'amount':amount})
                payment_guide=Payment_guide()
                payment_guide.user=user
                payment_guide.guide_order_id=order.get('id')    
                payment_guide.guide_amount=sum
                payment_guide.guide=guide_listitem
                payment_guide.save()
                print(payment_guide)
                
                dict_guide={
                    'order':order,
                    'user':user,
                    'sum':sum,
                }
                print(dict_guide)
                gd_id_list.delete()
    return render(request,'Travel_guide_booking_template/guidepayment.html',dict_guide)

@csrf_exempt
def gdbooked(request):
    if request.method=='POST':
        data_ofguide=request.POST
        
        print(data_ofguide)
        
        client.utility.verify_payment_signature(data_ofguide)
        razorpay_guide_order_id=data_ofguide['razorpay_order_id']
        razorpay_guide_payment_id=data_ofguide['razorpay_payment_id']
        payment_guide=Payment_guide.objects.get(guide_order_id=razorpay_guide_order_id)
        payment_guide.guide_payment_id=razorpay_guide_payment_id
        payment_guide.status=True
        
        print("hello")
        if Payment_guide.objects.filter(guide_payment_id=razorpay_guide_payment_id).exists():
            print("hell1")
        else:
            payment_guide.save()
            availabilityform_model=AvailabilityForm_Model.objects.all()
            for i in availabilityform_model:
                availabilityform_model_bk_start_date=i.bk_start_date
                availabilityform_model_bk_end_date=i.bk_end_date
                
            # form_data=request.session.get('form_data',{})
            # print(form_data)
            gd_book=Gd_booking(user=payment_guide.user,guide=payment_guide.guide,bk_start_date=availabilityform_model_bk_start_date,bk_end_date=availabilityform_model_bk_end_date,guide_book_active_status=True)
            gd_book.save()
            availabilityform_model.delete()
        
        return render(request,'Travel_guide_booking_template/gdbooked.html')
        
    return render(request,'Travel_guide_booking_template/gdbooked.html')

def Myguides(request):
    if request.method=='POST':
        cancel_book_guide=request.POST.get('cancel_book_guide')
        cancel_book_guide_object=Gd_booking.objects.get(id=cancel_book_guide)
        cancel_book_guide_object.guide_book_active_status=False
        cancel_book_guide_object.save()
        guide_cancelled=True
        if request.user.is_staff:
            gd_booking=Gd_booking.objects.all()
      
        else:
            gd_booking=Gd_booking.objects.filter(user=request.user)
        dict_myguide={
            'guide_cancelled':guide_cancelled,
            'gd_booking':gd_booking,
            }
    else:

        if request.user.is_staff:
            gd_booking=Gd_booking.objects.all()
        
        else:
            gd_booking=Gd_booking.objects.filter(user=request.user)
        dict_myguide={'gd_booking':gd_booking}

    return render(request,'Travel_guide_booking_template/Myguides.html',dict_myguide)

# def cancel_guide(request):
#     if request.method=='POST':
#         cancel_book_guide=request.POST.get('cancel_book_guide')
#         cancel_book_guide_object=Gd_booking.objects.get(id=cancel_book_guide)
#         cancel_book_guide_object.delete()
#         guide_cancelled=True
#     return render(request,'Travel_guide_booking_template/Myguides.html',{'guide_cancelled':guide_cancelled})