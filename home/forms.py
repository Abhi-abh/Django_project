from django import forms
from .models import Bookingm

class DateInput(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Bookingm
        fields = '__all__'
        widgets = {
        'booking_date': DateInput(),
    }
        labels = {
            'p_name' : 'Patient Name :',
            'p_phone' : 'Patient Phone no :',
            'p_email' : 'Patient Email :',
            'doc_name' : 'Doctor Name :',
            'booking_date' : 'Booking Date :',
        }