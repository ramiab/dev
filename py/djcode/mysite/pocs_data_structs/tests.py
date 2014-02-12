from unittest import TestCase
# from django.test import TestCase

# Create your tests here.
from data_structs_utils import bubble_sort, binary_search, _append_char_to_list, get_str_permutations, str_del_char


class DataStructTest(TestCase):
    def setup(self):
        pass


    def test_bubble_sort(self):
        l=[5,20,1,100,44,99,3]
        print l
        l1 = bubble_sort(l)
        print l1
        self.assertEqual( l1, [1, 3, 5, 20, 44, 99, 100])
        self.assertNotEqual( l1, l)


    def test_binary_search(self):
        l=[5,20,1,100,44,99,3]
        print l
        l1 = bubble_sort(l)
        print l1

        index = binary_search(l1, 0, len(l1)-1, 44)
        self.assertEqual( index, 4)

        index = binary_search(l1, 0, len(l1)-1, 30)
        self.assertEqual( index, -1)


    def test__append_char_to_list(self):
        l = ['bbc', 'bcd', 'aa']
        l1 = _append_char_to_list('a', l)
        self.assertEqual( l1, ['abbc', 'abcd', 'aaa'])

    def test_get_str_permutations(self):
        str = 'ab'
        l = get_str_permutations(str)
        print l
        self.assertEqual( len(l), 2)

        str = 'abc'
        l = get_str_permutations(str)
        print l
        self.assertEqual( len(l), 6)

        str = 'abcd'
        l = get_str_permutations(str)
        print l
        self.assertEqual( len(l), 24)


    def test_str_del_char(self):
        str = 'abcd'
        str2 = str_del_char(str, 2)
        print str2
        self.assertEqual( str2, 'abd')



