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

















