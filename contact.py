import pyperclip
class User:
    """
    Class that generates new instances of contacts.
    """
    contact_list = [] # Empty contact list

    def __init__(self,email,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            email: New contact email.
            username : New contact username.
            password: New contact password.
        '''
           # docstring removed for simplicity


        self.email = email
        self.username = username
        self.password = password
       
        contact_list = [] # Empty contact list
        
        # Init method up here
    def save_contact(self): 


        '''
        save_contact method saves contact objects into contact_list
        '''

        User.contact_list.append(self)

    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.contact_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a contact that matches that username.

        Args:
            username: username to search for
        Returns :
            Contact of person that matches the username.
        '''

        for contact in cls.contact_list:
            if contact.username == username:
                return contact

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list       

    @classmethod
    def copy_email(cls,username):
            contact_found = User.find_by_username(username)
            pyperclip.copy(contact_found.email)
            