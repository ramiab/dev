from django.test import TestCase
from linked_list import *
# Create your tests here.

class LinkedListTest(TestCase):
    def setup(self):
        head = Node(5, None)
        head = head.add_before(3)
        head = head.add_before(4)
        head = head.add_before(7)
        self.head = head.add_before(1)


    def test_node_add(self):
        print get_print_list_str(self.head)
        self.assertEqual(self.head.data, 1)

    def test_reverse_list_recursively(self):
            head = reverse_list_recursively(None, self.head)
            print get_print_list_str(head)
            self.assertEqual(head.data, 5)

    def test_reverse_list_iteratively(self):
            head = reverse_list_iteratively(self.head)
            print get_print_list_str(head)
            self.assertEqual(head.data, 5)


