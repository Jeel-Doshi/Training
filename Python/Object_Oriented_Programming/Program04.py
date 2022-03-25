# Create a class for Users,
# Username
# account no
# mobile no
# Address
# account balance
# -> Create a class for user manager
#     Manages user => Add new user, Get existing user, remove user
# -> Create a class for ATM,
# -> Enter account no and get user if not found then show a valid message
# -> Show options for user operations like creating new users, View Balance.        Deposit, Withdraw, Close account, etc...
# -> Transaction charge: 0.5 for every operation
# -> Account balance limit: 10000

class Users:

    def __init__(self,Username,account_no,mobile_no,Address,account_balance):
        self.Username = Username
        self.account_no = account_no
        self.mobile_no = mobile_no
        self.Address = Address
        self.account_balance = account_balance

class user_manager:
    
    def new_user(self):
        pass

    def get_existing_user(self):
        pass

    def remove_user(self):
        pass

class ATM:
    pass 