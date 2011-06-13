"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from wbinventory.tests.base import BaseTest


class ItemTest(BaseTest):

    fixtures = [
        'wbinventory_test_user.json',
        'wbinventory_test_item.json',
    ]

    def test_detail_shows_fields(self):
        c = self.logged_in_client()
        response = c.get('/wbinventory/items/2/')
        self.assertIn('67890', response.content)
        self.assertIn('six seven eight nine zero', response.content)
