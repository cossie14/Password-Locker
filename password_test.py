import unittest
from passwords import User
from passwords import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines tests for User class behaviours
    Args:
        unittest.TestCase: TestCase class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test instance
        '''
        self.new_user = User("Saudahabib","Instagram","trudet")# Instance of class User

    def test_init(self):
        '''
        Test case to test if object is initialised properly
        '''
        self.assertEqual(self.new_user.username, "Saudahabib")
        self.assertEqual(self.new_user.account, "Instagram")
        self.assertEqual(self.new_user.password, "trudet")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved to the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        '''
        tearDown does clear up after each test case has run
        '''
        User.user_list = []

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users in our user_list
        '''

        self.new_user.save_user()
        test_user = User("Mulki Suleiman", "Facebook", "trudet")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from object user_list
        '''
        self.new_user.save_user()
        test_user = User("Mulki Suleiman", "Facebook", "trudet")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_account(self):
        '''
        test to check if we can find a user by account
        '''

        self.new_user.save_user()
        test_user = User("Mulki Suleiman", "Facebook", "trudet")
        test_user.save_user()

        found_user = User.find_by_account("Facebook")
        self.assertEqual(found_user.account, test_user.account)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we don't find the user
        '''
        self.new_user.save_user()
        test_user = User("Mulki Suleiman", "Facebook", "trudet")
        test_user.save_user()
        user_exists = User.user_exists("Facebook")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)


if __name__ == '__main__':
    unittest.main()