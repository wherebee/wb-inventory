from django.contrib.auth.models import User
from django.test.client import Client
from django.test.testcases import TestCase


class BaseTest(TestCase):

    def logged_in_client(self):
        c = Client()
        logged_in = c.login(username='user', password='password')
        self.assert_(logged_in)
        return c
