from __future__ import unicode_literals
from django.http import JsonResponse
import json
from django.shortcuts import *
from student.models import Subject_table
from courses.models import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.template import RequestContext

def display_name(request):
    if(request.user.status=="Student"):
        all_subject = Subject_table.objects.filter(subject_university=request.session['user_university'])
        all_courses_name = Subject_table.objects.filter(subject_university=request.session['user_university'])
        student_name = request.user.nick_name
        list1 = []
        """list1 refers all the subjects' name"""
        list2 = []
        """list2 refers all the subjects' id"""
        list3 = []
        """list3 refers all the enrolled subjects' id """
        list4 = []
        """list4 refers all the enrolled subjects' name"""
        cur_id = str(request.user.id)

        my_courses = Courses_table.objects.filter(student_id_id=cur_id)

        for my_course in my_courses:
            list3.append(my_course.subject_id_id)

        for my_course_detail in my_courses:
            list4.append(my_course_detail.courses)

        for subject in all_subject:
            list1.append(subject.subject_name)
            list2.append(subject.subject_id)

        if request.method == 'POST':
            form1 = NameForm(request.POST)
            form2 = NameForm2(request.POST)

            if form2.is_valid():
                select_courses = list(form2.cleaned_data.values())
                Courses_table.objects.filter(student_id_id=cur_id, subject_id_id=select_courses[0]).delete()
                return render(request, 'student/studentprofile.html', {
                    'subjects': json.dumps(list1),
                    'ids': json.dumps(list2),
                    'my_subject_id': json.dumps(list3),
                    'my_subject_name': json.dumps(list4),
                    'name':student_name,
                    'sid': request.user.university,
                    'current_name': "",
                })

            if form1.is_valid():
                select_courses = list(form1.cleaned_data.values())
                for course in select_courses:
                    if course == 0:
                        return render(request, 'student/studentprofile.html', {
                            'subjects': json.dumps(list1),
                            'ids': json.dumps(list2),
                            'my_subject_id': json.dumps(list3),
                            'my_subject_name': json.dumps(list4),
                            'name': student_name,
                            'sid': request.user.university,
                            'current_name': "",
                        })

                for course in select_courses:
                    for my_course in list3:
                        if course == my_course:
                            return render(request, 'student/studentprofile.html', {
                                'subjects': json.dumps(list1),
                                'ids': json.dumps(list2),
                                'my_subject_id': json.dumps(list3),
                                'my_subject_name': json.dumps(list4),
                                'name': student_name,
                                'sid': request.user.university,
                                'current_name': "",
                            })

                name_list = []
                for id in select_courses:
                    for namess in all_courses_name:
                        if id == namess.subject_id:
                            name_list.append(namess.subject_name)

                Courses_table.objects.create(courses=name_list[0], student_id_id=cur_id,
                                                         subject_id_id=select_courses[0])



        return render(request, 'student/studentprofile.html', {
            'subjects': json.dumps(list1),
            'ids': json.dumps(list2),
            'my_subject_id': json.dumps(list3),
            'my_subject_name': json.dumps(list4),
            'name': student_name,
            'sid': request.user.university,
            'current_name': "",
        })
    else:
        all_subject = Subject_table.objects.filter(subject_university=request.session['user_university'])
        all_courses_name = Subject_table.objects.filter(subject_university=request.session['user_university'])
        student_name = request.user.nick_name
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        cur_id = str(request.user.id)

        my_courses = Courses_table.objects.filter(student_id_id=cur_id)

        for my_course in my_courses:
            list3.append(my_course.subject_id_id)
        # print(list3)

        for my_course_detail in my_courses:
            list4.append(my_course_detail.courses)

        for subject in all_subject:
            list1.append(subject.subject_name)
            list2.append(subject.subject_id)

        if request.method == 'POST':
            form1 = NameForm(request.POST)
            form2 = NameForm2(request.POST)

            if form2.is_valid():
                select_courses = list(form2.cleaned_data.values())
                Courses_table.objects.filter(student_id_id=cur_id, subject_id_id=select_courses[0]).delete()
                return render(request, 'student/teacherprofile.html', {
                    'subjects': json.dumps(list1),
                    'ids': json.dumps(list2),
                    'my_subject_id': json.dumps(list3),
                    'my_subject_name': json.dumps(list4),
                    'name': student_name,
                    'sid': request.user.university,
                    'current_name': "",
                })

            if form1.is_valid():
                select_courses = list(form1.cleaned_data.values())
                # print(select_courses)
                for course in select_courses:
                    if course == 0:
                        return render(request, 'student/teacherprofile.html', {
                            'subjects': json.dumps(list1),
                            'ids': json.dumps(list2),
                            'my_subject_id': json.dumps(list3),
                            'my_subject_name': json.dumps(list4),
                            'name': student_name,
                            'sid': request.user.university,
                            'current_name': "",
                        })

                for course in select_courses:
                    for my_course in list3:
                        if course == my_course:
                            return render(request, 'student/teacherprofile.html', {
                                'subjects': json.dumps(list1),
                                'ids': json.dumps(list2),
                                'my_subject_id': json.dumps(list3),
                                'my_subject_name': json.dumps(list4),
                                'name': student_name,
                                'sid': request.user.university,
                                'current_name': "",
                            })

                name_list = []
                for id in select_courses:
                    for namess in all_courses_name:
                        if id == namess.subject_id:
                            name_list.append(namess.subject_name)

                Courses_table.objects.create(courses=name_list[0], student_id_id=cur_id,
                                             subject_id_id=select_courses[0])

                # form2 = NameForm2(request.POST)

        return render(request, 'student/teacherprofile.html', {
            'subjects': json.dumps(list1),
            'ids': json.dumps(list2),
            'my_subject_id': json.dumps(list3),
            'my_subject_name': json.dumps(list4),
            'name': student_name,
            'sid': request.user.university,
            'current_name': "",
        })


def get_name(request):
    # if this is a POST request we need to process the form data
    #print("hello")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    #return render(request, 'name.html', {'form': form})
        return render(request, 'student/studentprofile.html')