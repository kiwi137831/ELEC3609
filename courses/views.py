from django.http import HttpResponse
from django.shortcuts import render, render_to_response,redirect
from courses.models import Courses_table
from student.models import Subject_table
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.template import RequestContext, context

def display_Course(request):
    #user need to login to see this site
    if request.user.id is not None:
        all_courses = Courses_table.objects.all()
        all_details = Subject_table.objects.all()
        list1 = [];
        list2 = [];
        list3 = [];
        for courses in all_courses:
            if courses.student_id_id == request.user.id:
                list1.append(courses.courses)
                list3.append(courses.subject_id_id)
        # print(list3)
        for id in list3:
            for details in all_details:
                if id == details.subject_id:
                    list2.append(details.subject_details)
                    continue

        #print(request.session['courses'])
        return render_to_response('courses/homepage.html',{'courses': json.dumps(list1),
                                                                'details': json.dumps(list2),
                                                                'courses_id': json.dumps(list3)})
    else:
        return redirect("http://127.0.0.1:8000/account/login/")