# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import New
# display list in admin page
class NewsAdmin(admin.ModelAdmin):	
	list_display = ('n_title', 'slug', 'n_date')
	search_fileds = ('title', 'n_content')
	prepopulated_fields = {'slug': ('n_title',)}
	date_hierarchy = 'n_date'
	ordering = [ 'n_date']

admin.site.register(New, NewsAdmin)