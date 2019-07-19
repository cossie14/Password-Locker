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


def main():
    print("Hello! Welcome to your Password Locker.Please sign up")
    while True:
        access_name = input("Password Locker Username: ").lower()
        if access_name == '':
            print("Wrong ")
        else:
            access_pass = getpass("Password Locker sign up key:  ")
            print("Log in using your sign-up credentials")
            login_name = input("Log in with your username: ").lower()
            login_pass = getpass("Please enter registered password: ")
            if access_pass == login_pass:
                print('\n')
                print(f"Welcome back {access_name}. What would you like to do?")
                print('\n')

            else:
                print("Invalid username or password!")

            while access_pass == login_pass:
                    print("Use these short codes : cc - create  new account credentials, dc - display account credentials, fc -find an account's credentials, ex -exit Password Locker, del - delete account credentials ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Account")
                            print("*"*100)

                            while True:
                                print ("Enter your account...")
                                account = input()

                                print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()


                                print("generated password or a customised? Type 1 for generated and  2 for customized...")

                                pass_choice = input().lower()

                                if pass_choice == 'c':
                                    print("Enter your password..")
                                    custom_pass = input()

                                    gene=custom_pass


                                elif pass_choice == '1':
                                    print("Password of your choice...")
                                    print('\n')
                                    print(generate_password())
                                    gene= generate_password()

                                if account == '' or username == '' or pass_choice == '':
                                    print("Account creation failed! Either Account, username or password is blank")
                                    print('\n')

                                else:
                                    save_user(create_user(username, account,gene)) # create and save new account.
                                    # save_user(create_user(username,account,custom_pass))

                                    print ('\n')
                                    print(f"New Credentials for {account} created")
                                    print ('\n')
                                break


                    elif short_code == 'del':
                        print("Delete account")
                        deli_user = input()
                        if check_existing_user(deli_user):
                            search_account = find_user(deli_user)
                            del_user(search_account)
                            print(f"{search_account.account} Account successfully deleted")

                    elif short_code == 'dc':

                            if display_users():
                                    print("Account credentials")
                                    print('\n')

                                    for user in display_users():
                                            print(f"First name:....{user.first name}")
                                            print(f"Last name:....{user.last name}")
                                            print(f"Password:....{user.password}")
                                            print(f" Account name: .....{user.account}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("Please create an account ")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the account ")

                            search_account = input()
                            if check_existing_user(search_account):
                                    search_account = find_user(search_account)
                                  print(f"{search_account.first_name} {search_account.last_name}")
                                    print('-' * 20)

                                    print(f"Account name: {search_account.account}")

                                    print('-' * 20)

                                    print(f"Password: {search_account.password}")

                            else:
                                    print("Account does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("Access Denied.Wrong Password")
            break

if __name__ == '__main__':

    main()
