import unittest #Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("Alekilexy","0727200709ak") # create contact object

    