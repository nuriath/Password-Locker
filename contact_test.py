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
        self.new_contact = User("queen@gmail.com","kingdom","jquery2") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.email,"queen@gmail.com")
        self.assertEqual(self.new_contact.username,"kingdom")
        self.assertEqual(self.new_contact.password,"jquery2")
        
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(User.contact_list),1)

# Items up here...

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
    User.contact_list = []
# other test cases here
    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = User("queen@gmail.com","kingdom","jquery2") # new contact
            test_contact.save_contact()
            self.assertEqual(len(User.contact_list),2)

            # More tests above
    

if __name__ == '__main__':
    unittest.main()