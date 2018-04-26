from django.db import models

# Create your models here.
class Subject_table(models.Model):
    subject_id = models.CharField(max_length=4, primary_key=True, default="000")
    subject_name = models.CharField(max_length=8, default="abc")
    subject_details = models.CharField(max_length=20, default = "abc")
    subject_university = models.CharField(max_length=20, default = "USYD")