from django import forms
from .models import cal

class DateInput(forms.DateInput):
    input_type = 'date'

class priceForm(forms.ModelForm):

	class Meta:
		model= cal
		fields = ('item_name','price','user_date',)
		widgets = {
            'user_date': DateInput(),
        }