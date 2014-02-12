from unittest import TestCase
# from django.test import TestCase

# Create your tests here.
from pocs_algorithms import plot_circle


class AlgorithmsTest(TestCase):
    def setup(self):
        pass


    def test_plot_circle(self):
        plot_circle(5)
        # self.assertEqual( l1, [1, 3, 5, 20, 44, 99, 100])
        # self.assertNotEqual( l1, l)

