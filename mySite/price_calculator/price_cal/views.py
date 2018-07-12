
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
from django.utils import timezone
from .models import cal
from .forms import priceForm
from django.template import Context,loader,RequestContext
from django.contrib import messages

# Create your views here.
"""def userPrice(request,pk):
	calcu=get_object_or_404(cal,pk=pk)
	in_date = pk.user_date
	out_date = pk.compare_date
	Diff=in_date-out_date
	if Diff.days<30:
		user_price=pk.price-(pk.price*0.06)
		return render(request,'price_cal/result.html',{'calcu':calcu})
	else:
		return render"""

def index(request):
	if request.method=="POST":
		form = priceForm(request.POST)
		if form.is_valid():
			calcu=form.save(commit=False)
			calcu.save()
			Diff= calcu.user_date-calcu.compare_date
			data = {'calcu':calcu,'Diff':Diff.days}
			if Diff.days<30:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.06)
			elif Diff.days>31 and Diff.days<90:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.12)

			elif Diff.days>91 and Diff.days<210:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.25)

			elif Diff.days>211 and Diff.days<365:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.50)

			elif Diff.days>366 and Diff.days<1095:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.62)
			
			elif Diff.days>1096 and Diff.days<2555:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.75)

			elif Diff.days>2556 and Diff.days<4380:
				data['user_price']=float(calcu.price)-(float (calcu.price)*0.95)
			return render(request, 'price_cal/result.html',data)
	else:
		form = priceForm()
	return render(request,'price_cal/index.html',{'form':form})

'''def userPriceCal(request,pk):
	calcu=get_object_or_404(cal,pk=pk)
	Diff=userDate()
	if Diff<30:
		user_price=pk.price-(pk.price*0.06)
		return render(request,'price_cal/result.html',{'calcu':calcu})
'''
