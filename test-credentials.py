import unittest
from credentials import credential

class TestCredentials(unittest.TestCase):
    """
    Test case that defines test cases for the credential class behaviour
    """

    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credentials = Credential("0727200709ak","twitter","Alekilexy","0727200709ak")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.view_password,"0727200709ak")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.login,"Alekilexy")
        self.assertEqual(self.new_credential.password,"0727200709jk")
    
    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saves into
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        """
        test_save_multiple_credential to check if one can save multiple credentials
        """
        self.new_credential.save_credential()
        test_credential = Credential("0788312907jk","test","login","0788312907jk")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete_contact to test if we can remove credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential ("0788312907jk","test","login","0788312907jk") # new credential
        test_credential.save_credential()

        self.new_credential.del_credential()# Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)

    def test_display_all_credentials(self):
        """
        test_display_all_credentials to returns a list of all credentials saved
        """
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()

