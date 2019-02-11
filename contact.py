class User:
    """
    Class that generates new instances of contacts.
    """
    contact_list = [] 

    def __init__(self,email,username,password):

        self.email = email
        self.username = username
        self.password = password
        
    # def create_contact(email,username,password):

    #     new_contact = User(email,username,password)


