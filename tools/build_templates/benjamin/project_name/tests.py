"""
python manage.py test
python manage.py core.SimpleTest
"""

from django.test import TestCase, Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)


