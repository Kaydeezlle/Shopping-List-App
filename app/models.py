''' This is a module with two classes namely users and shoppingList that can be used to create users
    log in users, create a shopping list, edit the shopping list, view the shopping list and delete 
    shopping list items'''


class Users(object):
    #the user class

    users = []
    def __init__(self, user_name=None, user_email=None, user_password=None):
        #User class variable initialization
        if user_name and user_password and user_email:
            self.user_name = user_name
            self.user_email = user_email
            self.user_password = user_password
            self.user_shopping_list = []
        else:
            self.user_name = None
            self.user_email = None
            self.user_password = None