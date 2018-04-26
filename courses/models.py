from django.db import models
from student.models import *
from account.models import *


class Courses_table(models.Model):
    student_id = models.ForeignKey(User)
    subject_id = models.ForeignKey(Subject_table)
    courses = models.CharField(max_length=8, default="abc")
    #courses_details = models.CharField(max_length=50, default="abc")

