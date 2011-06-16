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

    def test_edit_detail_success(self):
        c = self.logged_in_client()
        response = c.post('/wbinventory/items/1/edit/', {'number': '6-78901', 'name': 'another name'}, follow=True)
        self.assertIn('6-78901', response.content)
        self.assertIn('another name', response.content)
        self.assertNotIn('12345', response.content)
        self.assertNotIn('one two three four five', response.content)

    def test_edit_detail_failure_empty_number(self):
        c = self.logged_in_client()
        response = c.post('/wbinventory/items/1/edit/', {'number': '', 'name': 'another name'}, follow=True)
        self.assertIn('This field is required.', response.content)

    def test_edit_detail_failure_duplicate(self):
        c = self.logged_in_client()
        response = c.post('/wbinventory/items/1/edit/', {'number': '67890', 'name': 'another name'}, follow=True)
        self.assertIn('Item with this Number already exists.', response.content)
