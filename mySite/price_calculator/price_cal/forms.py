from django import forms
from .models import cal

class priceForm(forms.ModelForm):

	class Meta:
		model=cal
		fields = ('item_name','price','user_date',)