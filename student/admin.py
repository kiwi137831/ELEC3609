from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Subject_table

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'subject_name', 'subject_details','subject_university')
    #search_fileds = ('title', 'n_content')
    #subject_id = models.CharField(max_length=4, primary_key=True, default="000")
    #subject_name = models.CharField(max_length=8, default="abc")
    #subject_details = models.CharField(max_length=20, default="abc")
    #subject_university = models.CharField(max_length=20, default="USYD")
admin.site.register(Subject_table, SubjectsAdmin)