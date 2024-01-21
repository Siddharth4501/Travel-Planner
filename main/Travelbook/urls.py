from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signin/',views.signin,name="signin"),
    path('login/',views.handleLogin,name="login"),
    # path('payment/',views.payment,name='payment'),
    path('flight_user/',views.flight_user,name="flight_user"),
    path('signup/',views.handleSignup,name="signup"),
    path('bookingsearchresult/',views.bkr,name="bkr"),
    path('thanks/',views.thanks,name="thanks"),
    path('bookingreceipt/',views.bookingreceipt,name="bookingreceipt"),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('logout/',views.logOUT,name="logout"),
    path('bookedData/',views.bookedData,name='bookedData'),
    path('trail/',views.trail,name='trail'),
    path('weatherforecast/',views.weatherforecast,name='weatherforecast'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)