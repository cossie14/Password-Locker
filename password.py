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

