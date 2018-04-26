from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.IntegerField(primary_key = True)
    quizNo = models.IntegerField()
    order = models.IntegerField()
    description = models.CharField(max_length=200)
    firstAnswer = models.CharField(max_length=50)
    secondAnswer = models.CharField(max_length=50)
    thirdAnswer = models.CharField(max_length=50)
    fourthAnswer = models.CharField(max_length=50)
    correctAnswer = models.IntegerField()

    class Meta:
        db_table = 'Question'

class Quiz(models.Model):
    quizNo = models.IntegerField(primary_key=True)
    courseNo = models.CharField(max_length=8)

    class Meta:
        db_table = 'Quiz'