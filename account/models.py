from django.db import models

from django.contrib.auth.models import AbstractUser
# the user class is inherited from djamgo's user model and add nickname, university and status
class User(AbstractUser):
    nick_name = models.CharField(max_length=16)
    university = models.CharField(max_length=50,default='USYD')
    #status is used to decide the type of the account, we support two kinds, student and teacher right now with different rights in our system
    status = models.CharField(max_length=50, default='Student')