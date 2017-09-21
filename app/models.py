''' This is a module with two classes namely users and shoppingList that can be used to create users
    log in users, create a shopping list, edit the shopping list, view the shopping list and delete 
    shopping list items'''

USER_ID = 0
class Users(object):
    '''the user class'''

    users = []
    def __init__(self, user_name=None, user_email=None, user_password=None):
        '''User class variable initialization..'''
        if user_name and user_password and user_email:
            self.user_name = user_name
            self.user_email = user_email
            self.user_password = user_password
            self.user_shopping_list = []
        else:
            self.user_name = None
            self.user_email = None
            self.user_password = None

    def create_user(self, user_name, user_email, password):
        '''method for creating new users'''
        for user_object in self.users:
            if user_object.user_email == user_email:
                return "same email"
        for user_object in self.users:
            if user_object.user_name == user_name:
                return "same name"
        if user_name != "" and user_email != "" and password != "":
            user = Users(user_name, user_email, password)
            self.users.append(user)
            return "Okay"

    def login_user(self, user_email, password):
        '''method for logging in a user'''
        global USER_ID
        for member in self.users:
            if member.user_email == user_email and member.user_password == password:
                USER_ID = self.users.index(member)
                return True

    @classmethod
    def get_id(cls):
        '''A return user_id method.'''
        global USER_ID
        return USER_ID
            