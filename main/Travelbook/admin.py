from django.contrib import admin
from django.contrib.admin.sites import site



# Register your models here.
from Travelbook.models import Booking,Flights,bookeddata,Payment,bookeddata1,Booking_return
#class ContactAdmin(admin.ModelAdmin):
    #list_display=('username','email','phone','message')

#admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Flights)
admin.site.register(bookeddata)

admin.site.register(Payment)
admin.site.register(bookeddata1)
admin.site.register(Booking_return)
