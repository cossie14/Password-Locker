import random
import string

class User:
          """
          Class that generates new instances of users
          """

user_list = [] 

def __init__(self, first_name, last_name, account, password):


    self.first_name = first_name
    self.last_name = last_name
    self.account = account
    self.password = password


    def save_user(self):
        '''
        save_user method saves user names into the user list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes the user info from user_list
        '''
        User.user_list.remove(self)