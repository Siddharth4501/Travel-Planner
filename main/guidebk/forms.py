from django import forms 
from datetime import datetime
from django.contrib.sessions.models import Session

class AvailabilityForm(forms.Form):
    city=forms.CharField(max_length=50)
    bk_start_date=forms.DateTimeField(required=True,widget=forms.DateInput(attrs={'class':'form-control','type':"datetime-local",'min':'datetime.now()'}))
    bk_end_date=forms.DateTimeField(required=True,widget=forms.DateInput(attrs={'class':'form-control','type':"datetime-local"}))
    

    

        

