from unittest import TestCase
# from django.test import TestCase

# Create your tests here.
from str_int_conversion import convert_int_to_str, convert_str_to_int


class CalcTest(TestCase):
    def setup(self):
        pass


    def test_convert_int_to_str(self):
        s = convert_int_to_str(44678)
        self.assertEqual( s, '44678')

    def test_convert_str_to_int(self):
        s = convert_str_to_int('44678')
        self.assertEqual( s, 44678)



