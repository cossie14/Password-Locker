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

    @classmethod
    def find_by_account(cls,account):
        '''
        Method takes in account name and returns user info that matches that account
        Args:
            Account name to search for
        Returns:
            User info for that account
        '''
        for info in cls.user_list:
            if info.account == account:
                return info


    @classmethod
    def user_exists(cls,account):
        '''
        Method checks if user exists from the user_list
        Args:
            account : Account to search if user exists from user_list
        Return:
            Boolean: True or false depending if the user exists
        '''

        for user in cls.user_list:
            if user.account == account:
                return True

                   


@classmethod
def display_users(cls):
        '''
        Method that returns user list
        '''
        return cls.user_list

 class Credentials:
    
    '''
    Class  generates and saves credentials for users
    '''
       def __init__(firstname, account, password):
        self.password = password
        self.account = account

        def Password():
        chars = '111111111111111111111111111122222222222226666666666666'
        new_pass = ''.join(random.sample(chars, 5))
        return new_pass
       
