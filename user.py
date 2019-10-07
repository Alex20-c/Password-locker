class User:
    """
    Class that generates new instance of users
    """
    user_list=[]

    def __init__(self,username,password):
        self.username = username
        self.password = password
    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """
        User.user_list.append(self)

    @classmethod
    def find_by_number(cls,username):
        '''
        Method that takes in a username and returns a user matched that username.
        Args:
            username: username to search for
        Returns:
             user that matched the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user

        
        @classmethod
        def user_exist(cls,characters):
            """
            user_exists method that checks is a user exists fro m the user list
            args:
            characters:password to search is nthe user exists 
            returns:
                boolean:true or false depending on the condition
            """
            for user in cls.user_list:
                if user.password == characters:
                    return True


            return False




    
