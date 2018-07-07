
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import cal
from .forms import priceForm
# Create your views here.

def index(request):
	if request.method=="POST":
		form = priceForm(request.POST)
		if form.is_valid():
			TotalDay=timezone.now()-cal.objects.user_date
			if TotalDay<30:
				user_price=cal.objects.price-(cal.objects.price*0.06)
				messages.success(request, user_price)

			elif TotalDay>31 or TotalDay<90:
				user_price=cal.objects.price-(cal.objects.price*0.12)

			elif TotalDay>91 or TotalDay<210:
				user_price=cal.objects.price-(cal.objects.price*0.25)

			elif TotalDay>211 or TotalDay<365:
				user_price=cal.objects.price-(cal.objects.price*0.50)

			elif TotalDay>366 or TotalDay<1095:
				user_price=cal.objects.price-(cal.objects.price*0.62)
			
			elif TotalDay>1096 or TotalDay<2555:
				user_price=cal.objects.price-(cal.objects.price*0.75)

			elif TotalDay>2556 or TotalDay<4380:
				user_price=cal.objects.price-(cal.objects.price*0.95)
		return render(request,'price_cal/index.html',{'form':form})
	else:
		form = priceForm()
		return render(request,'price_cal/index.html',{'form':form})