import unittest

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        self.assertTrue(isEven(4))
    def testWrong(self):
        self.assertEqual(isEven(3), False)
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests        