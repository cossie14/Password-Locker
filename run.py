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