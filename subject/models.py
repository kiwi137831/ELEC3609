from django.db import models

# Create your models here.
from django.utils import timezone
from account.models import User
from student.models import *
from django.core.urlresolvers import reverse
from ckeditor.fields import *
#create manager to prepare for query function
class QuestionManager(models.Manager):
	def get_queryset(self):
		return super(QuestionManager, self).get_queryset().filter(status='published')
#create question data model
class Question(models.Model):
	STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
	Q_title = models.CharField(max_length=200)
	Q_des = RichTextField()
	create = models.DateTimeField(default=timezone.now)
	writer = models.ForeignKey(User, related_name='question_posts',null=True)
	course = models.ForeignKey(Subject_table,null=True)
	slug = models.SlugField(max_length=300, unique_for_date='create')
	Q_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')
	objects = models.Manager()
	likes_num = models.IntegerField(default=0)
	published = QuestionManager()

	# order question with date
	class Meta:
		ordering = ('-create',)

	# the default human-readable representation of the object
	def __str__(self):
		return self.Q_title

	# def  get_absolute_url(self,User,Courses_table):
	# 	return reverse('question:question_detail',
	# 	args=[User.id,Courses_table.id,self.id])

	# create answer data model
class Answer(models.Model):
	ans = models.ForeignKey(Question, related_name='answers')
	title = models.CharField(max_length=50)
	content = RichTextField()
	A_date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	allow = models.BooleanField(default=True)

	# order answer by created data
	class Meta:
		ordering = ('A_date',)

	# the default human-readable representation of the object
	def __str__(self):
		return 'Answer by {} on {}'.format(self.title, self.ans)