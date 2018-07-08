from django import forms
from .models import cal
from django.conf import settings
from django.utils import timezone
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class priceForm(forms.ModelForm):

	class Meta:
		model= cal
		fields = ('item_name','price','compare_date','user_date',)
	user_date = forms.DateField(
        widget=DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )	
	compare_date = forms.DateField(
        widget=DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y')
        )