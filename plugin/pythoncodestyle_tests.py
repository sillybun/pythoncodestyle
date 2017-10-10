import unittest
import pythoncodestyle as sut


class PythoncodestyleTests(unittest.TestCase):

    def test_easy_sample(self):
        input_source = ['import numpy as np', 'x = 3', 'y  = 4', 'z=[1,2,3,\
                        4]']
        actual_output = sut.style_code(input_source)
        expected_output = ['import numpy as np', 'x = 3', 'y = 4', 'z = [1, 2'
                           ', 3, 4]']
        self.assertEqual(actual_output, expected_output)

    def test_easy_sample2(self):
        input_source = ['x             = 1',
                        'y             = 2',
                        'long_variable = 3']
        actual_output = sut.style_code(input_source)
        expected_output = ['x = 1', 'y = 2', 'long_variable = 3']
        self.assertEqual(actual_output, expected_output)


unittest.main()
