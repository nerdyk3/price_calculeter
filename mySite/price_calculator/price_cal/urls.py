from django.conf.urls import include,url
from django.urls import path
from . import views


app_name = 'price_cal'

urlpatterns = [
	path('index/', views.index, name='index'),
]