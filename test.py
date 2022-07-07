'''import unittest
from testing import add, is_even 

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_is_even(self):
        self.assertTrue(is_even(2))

if __name__=='__main__':
    unittest.main()
'''

from testing import add,is_even

def test_add():
    assert add(2,3)==5
def test_is_even():
    assert is_even(2)==True

