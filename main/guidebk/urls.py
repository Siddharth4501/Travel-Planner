from django.urls import path
from guidebk import views
# from .views import BookingView

urlpatterns = [
    # path('book/',BookingView.as_view(),name='booking_view')
     path('bookgd/',views.BookingView,name='bookgd'),
     path('guidepayment/',views.guidepayment,name='guidepayment'),
     path('gdbooked/',views.gdbooked,name='gdbooked'),
     path('Myguides/',views.Myguides,name='Myguides'),
    #  path('cancel_guide/',views.cancel_guide,name='cancel_guide'),
]