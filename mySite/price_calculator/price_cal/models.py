from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class cal(models.Model):
	item_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	price = models.CharField(max_lenght=200)
	compare_date= models.DateField(default=timezone.now)
	user_date=models.DateField('user_date')

	def __str__(self):
		return self.price