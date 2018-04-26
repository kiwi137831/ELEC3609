# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone	
from django.contrib.auth.models import User

#create new data model
class New(models.Model):
	n_title = models.CharField(max_length=300)	
	slug = models.SlugField(max_length=300,	
		unique_for_date='n_date')	
	n_content = models.TextField()	
	n_date = models.DateTimeField(default=timezone.now)

	# order news according to date
	class Meta:	
		ordering = ('-n_date',)	

	# the default human-readable representation of the object
	def __str__(self):	
	 return self.n_title