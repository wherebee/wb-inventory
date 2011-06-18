"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from wbinventory.tests.base import BaseTest


class SiteSearchTest(BaseTest):

    fixtures = [
        'wbinventory_test_views_user.json',
        'wbinventory_test_views_sitesearch.json',
    ]

    def test_index_page_has_site_search(self):
        c = self.logged_in_client()
        response = c.get('/wbinventory/')
        self.assertIn('Search:', response.content)

    def test_search_shows_query(self):
        c = self.logged_in_client()
        response = c.get('/wbinventory/search/?q=something')
        # Check for the value we searched for being part of the input field.
        self.assertIn('value="something"', response.content)

    def test_search_page_with_results(self):
        c = self.logged_in_client()
        # One result.
        response = c.get('/wbinventory/search/?q=1')
        self.assertIn('12345', response.content)
        self.assertNotIn('67890', response.content)
        # Two results.
        response = c.get('/wbinventory/search/?q=e')
        self.assertIn('12345', response.content)
        self.assertIn('67890', response.content)

    def test_search_page_no_results(self):
        c = self.logged_in_client()
        response = c.get('/wbinventory/search/?q=doesnotexist')
        self.assertIn('No matching items.', response.content)

    def test_search_exact_match_found(self):
        """
        When an exact item number match is found, no form for creating
        a new item is shown.
        """
        c = self.logged_in_client()
        response = c.get('/wbinventory/search/?q=12345')
        self.assertNotIn('Create a new item', response.content)

    def test_search_exact_match_not_found(self):
        """
        When no exact item number match is found, a form for creating
        a new item is shown.
        """
        c = self.logged_in_client()
        response = c.get('/wbinventory/search/?q=24680')
        self.assertIn('Create a new item', response.content)
