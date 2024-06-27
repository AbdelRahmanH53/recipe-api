"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding number together"""
        res = calc.add(3,2)

        self.assertEqual(res,5)

    def test_subtract(self):
        """TESt Subtract numbers"""
        res = calc.subtract(15,10)
        self.assertEqual(res,5)