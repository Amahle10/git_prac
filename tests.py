import unittest
import my_python_project

class TestMyPytgonProject(unittest.TestCase):
    def testHandleInput(self):
        input = my_python_project.handle_input("abc")
        self.assertEqual('Wrong input', input)
        

if __name__ == '__main__':
    unittest.main()