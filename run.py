#!/usr/bin/env python3.6
from password import User
from password import Credentials
import random
from getpass import getpass

def create_user(username, account,password):
    '''
    Function to create a new user
    '''
    new_user = User(username, account,password)
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
    Function that finds a user by account name and returns the  user
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

def save_password(credentials):
    '''
    Function that saves new password
    '''
    return credentials.save_password()

def generate_password():
    '''
    Function that generates a password for the user
    '''
    return Credentials.generatePassword()

def main():
    print("Dear user!Welcome to Password Locker.")
    while True:
        access_name = input("Please enter your username here: ").lower()
        if access_name == '':
            print("Incorrect username")
        else:
            access_pass = getpass("Enter a secure password here:  ")
            print("Please log in to your account")
            login_name = input("Log in with your username: ").lower()
            login_pass = getpass("Please enter a registered password here: ")
            if access_pass == login_pass:
                print('\n')
                print(f"That is great {access_name}.Please choose an option?")
                print('\n')

            else:
                print("Sorry,try again!")

            while access_pass == login_pass:
                    print("Use these short codes : cc - create  new account credentials details, dc - display account credential details, fc -find an account's credential details, ex -exit , del - delete account credential details")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New account")
                            print("*"*30)

                            while True:
                                print ("Which account?...")
                                account = input()

                                print("Your username please? ...")
                                username = input()

                                print("Please choose an option,for generated password type g and for customised type c...")

                                pass_choice = input().lower()

                                if pass_choice == 'c':
                                    print("Enter a password here..")
                                    custom_pass = input()

                                    gene=custom_pass


                                elif pass_choice == 'g':
                                    print("please choose an option...")
                                    print('\n')
                                    print(generate_password())
                                    gene= generate_password()

                                if account == '' or username == '' or pass_choice == '':
                                    print("Sorry.Try again")
                                    print('\n')

                                else:
                                    save_user(create_user(username, account,gene)) 

                                    print ('\n')
                                    print(f"New Credential details for {account} created")
                                    print ('\n')
                                break


                    elif short_code == 'del':
                        print("Please enter the name of account to be deleted")
                        deli_user = input()
                        if check_existing_user(deli_user):
                            search_account = find_user(deli_user)
                            del_user(search_account)
                            print(f"{search_account.account} account successfully deleted")

                    elif short_code == 'dc':

                            if display_users():
                                    print("Account credential details list")
                                    print('\n')

                                    for user in display_users():
                                            print(f"Username:....{user.username}")
                                            print(f"password:....{user.password}")
                                            print(f" Account name: .....{user.account}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("Dear user,please create an account .")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Please enter the name of the account you want to search for")

                            search_account = input()
                            if check_existing_user(search_account):
                                    search_account = find_user(search_account)
                                    print(f"Username: {search_account.username}")
                                    print('-' * 30)

                                    print(f"Account name: {search_account.account}")

                                    print('-' * 30)

                                    print(f"Password: {search_account.password}")

                            else:
                                    print("Such account does not exist!")

                    elif short_code == "ex":
                            print("Bye.Have a blessed day .......")
                            break
                    else:
                            print("Incorrect.Try again")
            break
if __name__ == '__main__':
    main()

