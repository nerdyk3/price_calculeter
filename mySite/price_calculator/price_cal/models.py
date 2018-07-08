from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils import timezone
import datetime
from django.conf import settings


class cal(models.Model):
	item_name = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	compare_date= models.DateField(null=True)
	user_date= models.DateField(null=True)
	
	def __str__(self):
		return self.price


   