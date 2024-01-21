from django.contrib import admin
from .models import Guide,Gd_booking,Payment_guide,Gddata,AvailabilityForm_Model
# Register your models here.
admin.site.register(Guide)
admin.site.register(Gd_booking)
admin.site.register(Payment_guide)
admin.site.register(Gddata)
admin.site.register(AvailabilityForm_Model)