#!/usr/bin/env python3.6
from password import User
from password import Credentials
import random
from getpass import getpass

def create_user(first_name,last_name, account,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname, account,password)
    return new_user

def create_password(account, password):
    '''
    Function to create new password
    '''
    new_pass = Credentials(account, password)
    return new_pass

    def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()


    def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def find_user(account):
    '''
    Function that finds a user by account and returns the  user
    '''
    return User.find_by_account(account)


def check_existing_user(account):
    '''
    Function that checks if a user exists with that account and returns Boolean
    '''
    return User.user_exists(account)



def display_users():
    '''
    Function that returns all saved users
    '''
    return User.display_users()


def generate_password():
    '''
    Function that generates a password for the user
    '''
    return Credentials.generatePassword()


def save_password(credentials):
    '''
    Function that saves new password
    '''
    return credentials.save_password()

