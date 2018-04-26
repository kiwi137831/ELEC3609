from __future__ import unicode_literals
import datetime
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json
from django.shortcuts import render, render_to_response
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from .models import *
from account.models import *
from courses.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .form import *
from django.db import models
from django.shortcuts import redirect
from django.views.decorators.csrf import *
from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpResponse
from student.models import *
# Create your views here.


def question_list(request,subid):
    user =get_object_or_404(User,id=request.user.id)

    request.session['cur_subject']=subid

    course= get_object_or_404(Subject_table,subject_id=subid)
    q_list = Question.objects.filter(course=subid)
    user =request.user
    # add question
    Qform = QuestionForm(request.POST or None)
    if Qform.is_valid():
        nquestion=Qform.save(commit=False)
        nquestion.writer=user
        nquestion.course=course
        nquestion.save()
    # paging
    paginator = Paginator(q_list, 4)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)



    return render(request, 'subject/subject.html', {'questions': questions,'user':user,'course':course,'Qform':Qform,'user':user})

def question_detail(request,subid,qid):
    global guid
    # get question id
    question = get_object_or_404(Question,id=qid)
    user =get_object_or_404(User,id=request.user.id)
    course= get_object_or_404(Subject_table,subject_id=subid)
    # add answer


    Aform = AnswerForm(request.POST or None)
    if Aform.is_valid():
        instance = Aform.save(commit=False)
        instance.ans = question
        instance.save()
    answers = question.answers.filter(allow=True)
    instance = None
    # paging according to subject
    q_list = Question.objects.filter(course=subid)
    paginator = Paginator(q_list, 4)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

   #add question
    Qform = QuestionForm(request.POST or None)
    if Qform.is_valid():
        nquestion=Qform.save(commit=False)
        nquestion.writer=user
        nquestion.course=course
        if((nquestion.course!=None)and(nquestion.writer!=None)):
            nquestion.save()
    # return quesiton detail page.
    return render(request,
		'subject/details.html',
		{'question': question,
		'answers': answers,
		'new_answer': instance,
		'Aform': Aform,
         'questions': questions,
         'Qform': Qform,
         'user':user,
         'course':course,})


isLike = False
Nextq="a"

# like function
@csrf_exempt
def like(request):
    global  isLike
    qqid =request.POST.get('qqid')
    liken=int(request.POST.get('like_num'))
    q_list1 = Question.objects.filter(id=qqid)
    # if isLike == False:
    a = str(liken + 1)
    # isLike = True
    Question.objects.filter(id=qqid).update(likes_num=a)
#     elif isLike== True:
#         b = str(liken-1)
#         Question.objects.filter(id=qqid).update(likes_num=b)
#         isLike=False
# #


@csrf_exempt
def search(request):

    content = request.POST.get('content')
    questions = Question.objects.filter(course_id="1").filter(Q_title__icontains=content)
    qid_list = [];
    cid_list=[];
    for question in questions:
      qid_list.append(question.id)
      cid_list.append(question.course_id)
    # paginator = Paginator(questions, 4)
    # page = request.GET.get('page')
    # try:
    #     questions = paginator.page(page)
    # except PageNotAnInteger:
    #     questions = paginator.page(1)
    # except EmptyPage:
    #     questions = paginator.page(paginator.num_pages)
      serial =  serializers.serialize('json', questions.published.all())


    print(serial)
    return render_to_response('subject/details.html', {'q_list': json.dumps(questions)})



# @csrf_exempt
# def search(request):
#     global guid,gsubid,gqid
#     a=1
#     content = request.POST.get('content')
#     question =Question.objects.filter(course_id=a).filter(Q_title__icontains = content)
#
#     questionall = get_object_or_404(Question,id=gqid)
#     user =get_object_or_404(User,id=guid)
#     course= get_object_or_404(Courses_table,id=gsubid)
#
#     Aform = AnswerForm(request.POST or None)
#
#     if Aform.is_valid():
#         instance = Aform.save(commit=False)
#         instance.ans = question
#         instance.save()
#     answers = questionall.answers.filter(allow=True)
#     instance = None
#
#
#     q_list = Question.published.all()
#     paginator = Paginator(q_list, 4)
#     page = request.GET.get('page')
#     try:
#         questions = paginator.page(page)
#     except PageNotAnInteger:
#         questions = paginator.page(1)
#     except EmptyPage:
#         questions = paginator.page(paginator.num_pages)
#
#     Qform = QuestionForm(request.POST or None)
#     if Qform.is_valid():
#         nquestion=Qform.save(commit=False)
#         nquestion.writer=user
#         nquestion.course=course
#         if(nquestion.course!=None&nquestion.writer!=None):
#             nquestion.save()
#
#     return render(request,
#                   'subject/details.html',
#                   {'question': question,
#                    'answers': answers,
#                    'new_answer': instance,
#                    'Aform': Aform,
#                    'questions': questions,
#                    'Qform': Qform,
#                    'user': user,
#                    'course': course, })


# @csrf_exempt
# def search(request):
#     global guid,gsubid,gqid
#     a=1
#     content = request.POST.get('content')
#     question =Question.objects.filter(course_id=a).filter(Q_title__icontains = content)
#
#     return render(request,
#                   'subject/details.html',
#                   {'question': question,
#                    'answers': answers,
#                    'new_answer': instance,
#                    'Aform': Aform,
#                    'questions': questions,
#                    'Qform': Qform,
#                    'user': user,
#                    'course': course, })
