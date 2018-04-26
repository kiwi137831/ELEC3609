from django.test import TestCase
from quiz.views import *
from django.test import Client
from quiz.view_models import *

class SimpleTest(TestCase):
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
        response = self.client.post('/insert', {'courseNo':1, 'id':1, 'quizNo':1, 'order':2,
                                                'description': 'a test question', 'firstAnswer': 'a',
                                                'secondAnswer':'a', 'thirdAnswer':'รง','fourthAnswer':'d',
                                                'correctAnswer': 2, 'submit':'add and continue' })
        self.assertEqual(response.context['quizNo'], '1')
        self.assertEqual(response.context['new_order'], 3)
        self.assertEqual(response.context['new_id'], 1)
        self.assertEqual(response.context['courseNo'], '1')

    def test_get_all_quiz(self):
        response = self.client.post('/selectquiz/1/')
        quiz_list = Quiz.objects.all().filter(courseNo=1).order_by('quizNo')
        self.assertQuerysetEqual(response.context["all_quiz"], quiz_list)