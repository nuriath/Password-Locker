class User:
    """
    Class that generates new instances of contacts.
    """
    contact_list = [] 

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

        new_contact = User(user_name,password)

