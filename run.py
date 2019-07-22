#!/usr/bin/env python3.6
import random
from password import User
from password import Credentials
from getpass import getpass
import pyperclip

def create_user(firstname,lastname,password):
    '''
    Function to create user account
    '''
    new_user = User(firstname,lastname,password)
    return new_user

def save_user(user):
    '''
    Function to save new users
    '''
    User.save_user(user)

def authenticate_user(first_name,password):
    '''
    Function to verify user 
    '''
    confirm_user = Credential.confirm_user(first_name,password)
    return confirm_user

def generate_password():
    '''
    Function to generate password
    '''
    gen_pwd = Credential.generate_password()
    return gen_pwd

def create_credential(user_name,media,account_name,password):
    '''
    Function to create new credentials
    '''
    new_credential = Credential(user_name,media,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save new credentials
    '''
    Credential.save_credentials(credential)

def display_credentials():
    '''
    Function to display_credentials saved
    '''
def copy_password(media):
    '''
    Function to copy credentials and paste them in clipboard
    '''
    return Credential.copy_password(media)





def main():
    print("Hello! Welcome to Password Locker.")
    while True:
        access_name = input("Enter your firstname here: ").lower()
        if access_name == '':
            print("Invalid username")
        else:
            access_pass = getpass("Enter a password here:  ")
            print("Log in ")
            login_name = input("Log in with your username: ").lower()
            login_pass = getpass("Please enter registered password: ")
            if access_pass == login_pass:
                print('\n')
                print(f"Welcome back {access_name}. Choose an option")
                print('\n')

            else:
                print("Invalid username or password!")

            while access_pass == login_pass:
                    print("Use these short codes : cc - create  new account credentials, dc - display account credentials, fc -find an account's credentials, ex -exit , del - delete account credentials ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Account")
                            print("*"*80)

                            while True:
                                print ("Which account ?...")
                                account = input()

                                print("What's your username? ...")
                                username = input()

                                print("Choose an option, generated password or a customised? Type c for customised and g for generated...")

                                pass_choice = input().lower()

                                if pass_choice == 'c':
                                    print("Enter a password here..")
                                    custom_pass = input()

                                    gene=custom_pass


                                elif pass_choice == 'g':
                                    print("Here's a password we think will work for you...")
                                    print('\n')
                                    print(generated_password())
                                    gene= generated_password()

                                if account == '' or username == '' or pass_choice == '':
                                    print("Account creation failed! Either Account, username or password is blank")
                                    print('\n')

                                else:
                                    save_user(create_user(username, account,gene)) 

                                    print ('\n')
                                    print(f"New Credentials for {account} created")
                                    print ('\n')
                                break


                    elif short_code == 'del':
                        print("Enter name of account to be deleted")
                        deli_user = input()
                        if check_existing_user(deli_user):
                            search_account = find_user(deli_user)
                            del_user(search_account)
                            print(f"{search_account.account} account credentials successfully deleted")

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is a list of all your account credentials")
                                    print('\n')

                                    for user in display_user():
                                            print(f"Username:....{user.username}")
                                            print(f"password:....{user.password}")
                                            print(f" Account name: .....{user.account}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("Please create an account first.")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the account you want to search for")

                            search_account = input()
                            if check_existing_user(search_account):
                                    search_account = find_user(search_account)
                                    print(f"Username: {search_account.username}")
                                    print('-' * 50)

                                    print(f"Account name: {search_account.account}")

                                    print('-' * 50)

                                    print(f"Password: {search_account.password}")

                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("Ooops! Please try again")
            break


if __name__ == '__main__':
    main()
