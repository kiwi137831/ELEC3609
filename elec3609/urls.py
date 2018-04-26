"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from welcomepage.views import *
from courses.views import *
from student.views import *
from news.views import *
from quiz import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^welcomepage', welcomepage),
    url(r'^homepage/', display_Course),
    url(r'^news/', display_news),
    url(r'^studentprofile/$',display_name),
    url(r'^subject/', include('subject.urls', namespace='question', app_name='subject')),

    url(r'^insert$', csrf_exempt(views.insert)),
    url(r'^quiz$', csrf_exempt(views.list)),
    url(r'^selectquiz/(?P<cid>\d+)/', csrf_exempt(views.get_all_quiz)),
    url(r'^score$',csrf_exempt(views.score)),
    url(r'^choose_to_add/(?P<cid>\d+)$',csrf_exempt(views.add_all_quiz)),
    url(r'^submit_answers$', csrf_exempt(views.check_answers)),
    url(r'^question_to_insert$', csrf_exempt(views.question_to_insert)),
]
