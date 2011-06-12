"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


class SiteSearchTest(TestCase):

    def logged_in_client(self):
        u = User.objects.create_user('user', 'user@example.com', 'password')
        c = Client()
        logged_in = c.login(username='user', password='password')
        self.assert_(logged_in)
        return c

    def test_index_page_has_site_search(self):
        c = self.logged_in_client()
        response = c.get('/wbinventory/', follow=True)
        assert 'Search:' in response.content
