from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import register


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
