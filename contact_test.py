import unittest # Importing the unittest module
from contact import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = User("Queen@gmail.com","kingdom","jquery2") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.email,"Queen@gmail.com")
        self.assertEqual(self.new_contact.username,"kingdom")
        self.assertEqual(self.new_contact.phone_number,"jquery2")
       
