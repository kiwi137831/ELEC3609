from .models import Answer,Question
from ckeditor.fields import *
#create answer form
class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('title', 'content','allow')
#create form to contain question title
class AnswerForms(forms.Form):
	Q_title = forms.CharField(max_length=200)
	Q_des = RichTextField()
	slug = forms.SlugField(max_length=300)

#create form of question
class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields=('Q_title','Q_des','slug','status',)