
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import cal
from .forms import priceForm
# Create your views here.

def index(request):
	if request.method=="GET":
		form = priceForm(request.GET)
		if (form.is_valid()):
			TotalDay=userDate()
			if TotalDay<30:
				user_price=cal.objects.price-(cal.objects.price*0.06)
				userPrice(user_price)
			elif TotalDay>31 or TotalDay<90:
				user_price=cal.objects.price-(cal.objects.price*0.12)
				userPrice(user_price)
			elif TotalDay>91 or TotalDay<210:
				user_price=cal.objects.price-(cal.objects.price*0.25)
				userPrice(user_price)
			elif TotalDay>211 or TotalDay<365:
				user_price=cal.objects.price-(cal.objects.price*0.50)
				userPrice(user_price)
			elif TotalDay>366 or TotalDay<1095:
				user_price=cal.objects.price-(cal.objects.price*0.62)
				userPrice(user_price)
			elif TotalDay>1096 or TotalDay<2555:
				user_price=cal.objects.price-(cal.objects.price*0.75)
				userPrice(user_price)
			elif TotalDay>2556 or TotalDay<4380:
				user_price=cal.objects.price-(cal.objects.price*0.95)
				userPrice(user_price)
	else:
		form = priceForm()
	return render(request,'price_cal/index.html',{'form':form})

def userDate(request):
	isValid = False
	while not isValid:
	   	in_date = cal.user_date
	   	out_date = cal.compare_date
	   	try:
	   		d = strptime(in_date, '%d/%m/%Y')
	   		g = strptime(out_date, '%d/%m/%Y')
	   		isValid = True
	   	except :
	   		print("this is not the right")
	diff= g-d
	return(diff)

def userPrice(user_price):
	return render_to_response('result.html',context_instance=RequestContext(request,{'user_price':user_price}))