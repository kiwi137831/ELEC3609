from .view_models import *
from django.shortcuts import render,render_to_response

# Get the question through POST httprequest and store it in the database
# Whenever the question No is 1, a new quiz is created
def insert(request):
    if request.method == "POST":
        id = request.POST.get("id", None)
        quizNo = request.POST.get("quizNo", None)
        order = request.POST.get("order", None)
        description = request.POST.get("description", None)
        firstAnswer = request.POST.get("firstAnswer", None)
        secondAnswer = request.POST.get("secondAnswer", None)
        thirdAnswer = request.POST.get("thirdAnswer", None)
        fourthAnswer = request.POST.get("fourthAnswer", None)
        correctAnswer = int(request.POST.get("correctAnswer", None))
        courseNo = request.POST.get("courseNo", None)
        # Create a question object and store in database
        question_tosave = Question.objects.create(id=id, quizNo=quizNo, order=order, description=description,firstAnswer=firstAnswer,
                                    secondAnswer=secondAnswer, thirdAnswer=thirdAnswer,
                                    fourthAnswer=fourthAnswer, correctAnswer=correctAnswer)
        question_tosave.save()

        # Create a quiz object and store in database
        if int(order) == 1:
            quiz_tosave = Quiz.objects.create(quizNo=quizNo, courseNo=courseNo)
            quiz_tosave.save()
        submit = request.POST.get("submit", None)

        # When a user clicks "add and continue", stay in the current page
        if submit == "add and continue":
            new_order = int(order)+1
            new_id = int(id)+1
            return render_to_response('quiz/insert_to_quiz.html', {"quizNo": quizNo, "new_order": new_order,
                                                              "new_id": new_id, "courseNo": courseNo})

        # When a user clicks "add and quit", go back to the previous page
        elif submit == "add and quit":
            all_quiz = Quiz.objects.all().filter(courseNo=courseNo).order_by('quizNo')
            return render_to_response("quiz/choose_to_add.html", {"all_quiz": all_quiz, "courseNo": courseNo})
    else:
        return render_to_response('quiz/failure.html')

# Get the questions according to the users choice from database
def list(request):
    if request.method == "POST":
        quizNo = request.POST.get("quizNo",None)
        questions = Question.objects.all().filter(quizNo=quizNo).order_by('quizNo')
        return render_to_response("quiz/quiz.html", {"data": questions, "quizNo":quizNo})
    return render_to_response('quiz/quiz.html')

# Get all the quizzes according to the course id and direct to thee first page for student to choose a quiz to do
def get_all_quiz(request,cid):
    courseNo=cid
    print(courseNo)
    all_quiz = Quiz.objects.all().filter(courseNo=courseNo).order_by('quizNo')
    return render_to_response("quiz/selectQuiz.html", {"all_quiz":all_quiz})

# Get all the quizzes according to the course id and direct to the first page for teacher to add question into quiz
def add_all_quiz(request,cid):
    courseNo =cid
    print(courseNo)
    all_quiz = Quiz.objects.all().filter(courseNo=courseNo).order_by('quizNo')
    return render_to_response("quiz/choose_to_add.html", {"all_quiz":all_quiz, "courseNo":courseNo})

# Direct to the quiz page
def score(request):
    return render_to_response('quiz/quiz.html')

# Check the answers submited by student and show the questions
# are wrong with the corresponding wrong and correct answers
def check_answers(request):
    if request.method=="POST":
        quizNo = request.POST.get("quizNo", None)
        data = Question.objects.all().filter(quizNo=quizNo).order_by('quizNo')
        correct_count = 0;
        total_count = 0;
        answer_list = {}
        for line in data:
            order = line.order
            answer = request.POST.get(str(order), None)
            if int(line.correctAnswer) == int(answer):
                correct_count += 1
            else:
                # Get the correct answer from database according to the submission from student
                correct_answer = ""
                if int(line.correctAnswer) == 1:
                    correct_answer = line.firstAnswer
                elif int(line.correctAnswer) == 2:
                    correct_answer = line.secondAnswer
                elif int(line.correctAnswer) == 3:
                    correct_answer = line.thirdAnswer
                elif int(line.correctAnswer) == 4:
                    correct_answer = line.fourthAnswer

                # Combine the correct answer and wrong answer and return it as a string
                if int(answer) == 1:
                    answer_list[str(line.description)] = str(line.firstAnswer) + "_" + correct_answer
                elif int(answer) == 2:
                    answer_list[str(line.description)] = str(line.secondAnswer) + "_" + correct_answer
                elif int(answer) == 3:
                    answer_list[str(line.description)] = str(line.thirdAnswer) + "_" + correct_answer
                elif int(answer) == 4:
                    answer_list[str(line.description)] = str(line.fourthAnswer) + "_" + correct_answer

            total_count += 1
        return render_to_response("quiz/score.html", {"data": data, "correct_count": correct_count,
                                                         "total_order": total_count, "answer_list": answer_list})

# Get the new id, questionNo and quizID for the new question that is ready to add
def question_to_insert(request):
    if request.method == "POST":
        new_quiz = request.POST.get("new_quiz", None)
        course_no = request.POST.get("courseNo", None)
        new_id = 1
        if int(new_quiz) == 0:
            quizNo = request.POST.get("quizNo", None)
            # Get the question No and the"new No" = largest No + 1
            all_question_order = Question.objects.all().filter(quizNo=quizNo).order_by("order").reverse()
            new_order = 1
            if all_question_order:
                new_order = int(all_question_order[0].order) + 1
            # Get the question id and the "new id" = largest id + 1
            all_question_id = Question.objects.all().order_by("id").reverse()
            new_id = 1
            if all_question_id:
                new_id = str(int(all_question_id[0].id) + 1)
            return render_to_response('quiz/insert_to_quiz.html', {"quizNo": quizNo, "new_order": new_order,
                                                              "new_id": new_id, "courseNo": course_no})
        # When a new quiz is created, quizNo + 1 and question No = 1. question_id = largetst id + 1
        elif int(new_quiz) == 1:
            all_quizNo = Quiz.objects.all().order_by("quizNo").reverse()
            new_quizNo = 1
            if all_quizNo:
                new_quizNo = int(all_quizNo[0].quizNo) + 1
            new_order = 1;
            all_question_id = Question.objects.all().order_by("id").reverse()
            if all_question_id:
                new_id = str(int(all_question_id[0].id) + 1)
            return render_to_response('quiz/insert_to_quiz.html', {"quizNo": new_quizNo, "new_order":new_order,
                                                      "new_id":new_id, "courseNo": course_no})
    else:
        return None
