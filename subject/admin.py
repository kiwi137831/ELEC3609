from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Answer
# Create Question model in the admin function
class questionAdmin(admin.ModelAdmin):
	list_display = ('Q_title', 'slug', 'writer', 'create','status')
	list_filter = ('create', 'Q_date', 'writer')
	search_fields = ('Q_title', 'Q_des')
	prepopuplated_fields = {'slug': ('Q_title',)}
#	raw_id_fields = ('writer',)
	date_hierarchy = 'create'
	ordering = ['status', 'create']

admin.site.register(Question, questionAdmin)
# Create Answer model in the admin function
class AnswerAdmin(admin.ModelAdmin):
	list_display = ('title', 'ans', 'A_date', 'allow')
	list_filter = ('allow', 'A_date', 'update')
	search_fields = ('title', 'content')
admin.site.register(Answer, AnswerAdmin)