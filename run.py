#!/usr/bin/env python3.6
from contact import User
def create_contact(email,username,password):
        '''
        Function to create a new contact
        '''
        new_contact = User(email,username,password)
        return new_contact

def save_contacts(contact):
        '''
        Function to save contact
        '''
        contact.save_contact()

def del_contact(contact):
        '''
        Function to delete a contact
        '''
        contact.delete_contact()    

def find_contact(username):
        '''
        Function that finds a contact by username and returns the contact
        '''
        return User.find_by_username(username)


def check_existing_contacts(username):
        '''
        Function that check if a contact exists with that username and return a Boolean
        '''
        return User.contact_exist(username)

def main():
    print("Hello Welcome to your contact list. What is your name?")
    
            username = input()

            print(f"Hello {username}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print("email ...")
                            e_address = input()

                            print ("username ....")
                            f_name = input()

                            print("password ...")
                            l_name = input()

                            save_contacts(create_contact(email,username,password)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {email} {username} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.email} {contact.username} .....{contact.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_username = input()
                            if check_existing_contacts(search_username):
                                    search_contact = find_contact(search_username)
                                    print(f"{search_contact.email} {search_contact.password}")
                                    print('-' * 20)

                                    print(f"username.......{search_contact.username}")
                                    print(f"email.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")















