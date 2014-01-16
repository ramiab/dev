from unittest import TestCase
# from django.test import TestCase
from calculator import get_next_element_str, get_brackets_expression
from calculator import calc

# Create your tests here.

class CalcTest(TestCase):
    def setup(self):
        pass


    def _test_get_next_element_str(self, expression, expected_elem, expected_suffix):
        elem, suffix = get_next_element_str(expression)
        print "elem = %s ; suffix = %s" % (elem, suffix)
        self.assertEqual(expected_elem, elem)
        self.assertEqual(expected_suffix, suffix)
        return elem, suffix

    def test_get_next_element_str(self):
        expression ="33+4*5/6-99"
        elem, suffix = self._test_get_next_element_str(expression,"33","+4*5/6-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"+","4*5/6-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"4","*5/6-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"*","5/6-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"5","/6-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"/","6-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"6","-99" )
        elem, suffix = self._test_get_next_element_str(suffix,"-","99" )
        elem, suffix = self._test_get_next_element_str(suffix,"99","" )

    def test_get_brackets_expression(self):
        result = get_brackets_expression("(33+4)*5/6-99")
        print result
        self.assertEqual("33+4", result)

        result = get_brackets_expression("((33+4)*5/6)-99")
        print result
        self.assertEqual("(33+4)*5/6", result)

    def test_calc(self):
        result = calc("33+4*5/6-99")
        print result
        self.assertEqual(-62.666666666666664, result)

    def test_calc1(self):
        result = calc("(33+4)*5/6-99")
        print result
        self.assertEqual(-68.16666666666667, result)



