"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from models import CmdJob

class SimpleTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
        unittest.main()