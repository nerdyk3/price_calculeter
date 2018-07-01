from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import cal
# Create your views here.

def index(request,self,user_price):
	return render(request,'price_cal/post_price.html',{})

def Date_cal(request, user_date):
	LastDate=cal.object.user_date
	TodayDate=timezone.now
	TotalDay=TodayDate-LastDate
	self.price(TotalDay)

def price(request,price,self,TotalDay):
	if TotalDay<30:
		user_price=cal.object.price-(cal.object.price*0.06)

	elif TotalDay>31 or TotalDay<90:
		user_price=cal.object.price-(cal.object.price*0.12)

	elif TotalDay>91 or TotalDay<210:
		user_price=cal.object.price-(cal.object.price*0.25)

	elif TotalDay>211 or TotalDay<365:
		user_price=cal.object.price-(cal.object.price*0.50)

	elif TotalDay>366 or TotalDay<1095:
		user_price=cal.object.price-(cal.object.price*0.62)
	
	elif TotalDay>1096 or TotalDay<2555:
		user_price=cal.object.price-(cal.object.price*0.75)

	elif TotalDay>2556 or TotalDay<4380:
		user_price=cal.object.price-(cal.object.price*0.95)
	
	self.index('user_price')