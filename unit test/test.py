from django.test import TestCase
from account.models import User
from courses.models import Courses_table
from student.models import Subject_table
from django.test import Client
from quiz.view_models import  Quiz
from news.models import New
from subject.models import Question
class MyTest(TestCase):
    def setUp(self):
        User.objects.create(username="test",password="123",email="123@123.com",nick_name="testuser",university="USYD")
        Subject_table.objects.create(subject_id="123",subject_name="ELEC3609",
                                     subject_details="Test",subject_university="USYD")
        self.client = Client()

    def test_case1(self):
        testuser = User.objects.get(id="1")
        #self.assertEqual(testuser.nick_name,"testuser")
        client = Client()
        client.login(username=testuser.username, password=testuser.password)
        s = client.session
        s['cur_user_id'] = testuser.id
        s.save()
        self.assertEqual(s['cur_user_id'],1)
    def test_case2(self):
        testsubject = Subject_table.objects.get(subject_id="123")
        self.assertEqual(testsubject.subject_name,"ELEC3609")


class QuizTest(TestCase):
    def setup(self):
        self.client = Client()
        quiz_tosave = Quiz.objects.create(quizNo=1, courseNo=1)
        quiz_tosave.save()

    def test_choose_to_add(self):
        response = self.client.post('/choose_to_add/1/')
        quiz_list = Quiz.objects.all().filter(courseNo=1).order_by('quizNo')
        self.assertQuerysetEqual(response.context["all_quiz"], quiz_list)
        self.assertEqual(response.context["courseNo"], '1')

    def test_insert(self):
        response = self.client.post('/insert', {'courseNo':1, 'id':2, 'quizNo':1, 'order':2,
                                                'description': 'a test question', 'firstAnswer': 'a',
                                                'secondAnswer':'a', 'thirdAnswer':'ç','fourthAnswer':'d',
                                                'correctAnswer': 2, 'submit':'add and continue' })
        self.assertEqual(response.context['quizNo'], '1')
        self.assertEqual(response.context['new_order'], 3)
        self.assertEqual(response.context['new_id'], 3)
        self.assertEqual(response.context['courseNo'], '1')

    def test_get_all_quiz(self):
        response = self.client.post('/selectquiz/1/')
        quiz_list = Quiz.objects.all().filter(courseNo=1).order_by('quizNo')
        self.assertQuerysetEqual(response.context["all_quiz"], quiz_list)


class SubjectTest(TestCase):
    def setup(self):
        self.client = Client()
        Question_tosave = Question.objects.create(Q_title="test", Q_des="example",
                                                   slug="test", status="published",course_id=1)
        testuser = User.objects.create(username="testuser", email="111@111.com", nick_name="testname",
                                       password="123",status="Student",university="USYD")
        testsubject = Subject_table.objects.create(subject_id=1, subject_name="ELEC3609", subject_details="example", subject_university="USYD")
        testsubject.save()
        Question_tosave.save()
    def test_list(self):
        response = self.client.post('/subject/1', name='question_list')

        self.assertEqual(response.context['questions'], "testuser")

class NewsTest(TestCase):
    def setup(self):
        self.client = Client()
        news_tosave = New.objects.create( n_title = 'test', slug = 'sluggg', n_content = 'this is some text',
                                         n_date = datetime.now())
        news_tosave.save()
        news_tosave.refresh_from_db()

    def test_display_news(self):
        response = self.client.post('/news/')
        news_list = response.context['news_list'][0]
        self.assertEqual(news_list['n_title'], 'test')
        self.assertEqual(news_list['slug'], 'sluggg')
        self.assertEqual(news_list['news_context'], 'this is some text')
        self.assertEqual(news_list['news_date'], '11-03-17')

class CourseTest(TestCase):
    def setup(self):
        self.client = Client()
        user = User.objects.create(nickname='leo', university='USYD', status='student')
        user.save()
        subject = Subject_table.objects.create(subject_id='001', subject_name='info1111', subject_details='lol',
                                               subject_university='USYD')
        subject.save()
        course = Courses_table.object.create(student_id=user, subject_id=subject, courses='info1111')
        course.save()

    def test_display_Course(self):
        response = self.client.get('/homepage/')
        self.assertEqual(response.context['courses'], 'info1111')
        self.assertEqual(response.context['details'], 'lol')
        self.assertEqual(response.context['courses_id'], '001')