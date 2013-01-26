"""
python manage.py test
python manage.py core.SimpleTest
"""

from django.test import TestCase, Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

class ExampleResponseViewTester(TestCase):
    def setUp(self):
        self.client = Client() 
        self.response = self.client.get('/example_response')

    def test_example_response():
        self.assertEqual(self.response.content, "Nice example!")

