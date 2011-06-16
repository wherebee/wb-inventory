from django.test.client import Client
from django.test.testcases import TransactionTestCase


class BaseTest(TransactionTestCase):

    def logged_in_client(self):
        c = Client()
        logged_in = c.login(username='user', password='password')
        self.assert_(logged_in)
        return c
