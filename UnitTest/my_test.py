import unittest

import my_program

class MyTest(unittest.TestCase):
    def test_one(self):
        input = 15
        output = 4
        result = my_program.count_set_bits(input)
        self.assertEqual(result,output)
    
    def test_two(self):
        input = 24
        output = 2
        result = my_program.count_set_bits(input)
        self.assertEqual(result,output)


if __name__ == "__main__":
    unittest.main()