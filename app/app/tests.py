"""
sample test

"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """calculator add two values testing"""
    def test_add_two_number(self):
        """ testing"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_two_number(self):
        """substract two no"""
        res = calc.sub(5, 3)
        self.assertEqual(res, 2)
