import unittest
from note import 


class MyTestCase(unittest.TestCase):
  def setUp(self):
    self.test = ['Andela','test' , 'testThree']

    def test_object_(self):
    	test_obj= NotesApplication('someone')
    	assertEqual(True,type(test_obj) is NotesApplication)

    def test_instance(self):
        test_obj = NotesApplication()
        with self.asserRaises(	)	
