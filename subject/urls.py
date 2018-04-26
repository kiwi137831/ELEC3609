from django.conf.urls import url, include

from subject import views
import subject
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    #question detail display
    url(r'^(?P<subid>\d+)/(?P<qid>\d+)$', views.question_detail,
        name='question_detail'),
    # views of question
    url(r'^(?P<subid>\d+)$', views.question_list,name='question_list'),
    #dirction of like
    url(r'^like/', views.like),



]
