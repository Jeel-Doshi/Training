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

class Manager:
    
    def add_new_user(self):
        new_user()
        print("Welcome..! You are now the user of the Bank..! ")

    def get_existing_user(self):
        print("Existing users are as follows: ")
        for user in data:
            print(user)
        print()

    def remove_user(self):
        user_account = input("Enter account number ")
        for user in data:
            if user_account == data[user]["Account Number"]: 
                data.pop(user)
                print("User removed successfully ")
                break
            else:
                print("No User with this Account Number ")

class ATM:
    
    def get_account_number(self):
        account_number = input("Enter account number ")
        for user in data:
            for detail in data[user]:
                if account_number == data[user][detail]:
                    print("Your current balance is {} ".format(data[user]['Account Balance']))
                    break
            else:
                print("No user found ")

    def view_balance(self):
        account_number = input("Enter account number ")
        for user in data:
            for detail in data[user]:
                if account_number == data[user][detail]:
                    print("Your current balance is {} ".format(data[user]['Account Balance']))
                    break
            else:
                print("No user found ")
                
    def deposit_withdraw(self):

        user_input = input("Enter 1 to deposit\nEnter 2 to withdraw\n")
        if user_input == '1':
            account_number = input("Enter your account number ")
            for user in data:
                for detail in data[user]:
                    if account_number == data[user][detail]: 
                        amount = input("Enter amount to deposit ")
                        balance = int(data[user]['Account Balance']) + int(amount)
                        print("Your new balance is {} ".format(balance))
                        data[user]["Account Balance"] = balance
                        break
                else:
                    print("No user found ")

        elif user_input == '2':
            account_number = input("Enter your account number ")
            for user in data:
                for detail in data[user]:
                    if account_number == data[user][detail]: 
                        amount = input("Enter amount to withdraw ")
                        if int(data[user]["Account Balance"]) - int(amount) <= 0:
                            print("Insufficient balance ")
                            break
                        else:
                            balance = int(data[user]["Account Balance"]) - int(amount) - 0.5
                            print("Your new balance is {} ".format(balance))
                            data[user]["Account Balance"] = balance
                            break
                else:
                    print("No user found ") 
        else:
            print("Enter valid number ")

print("Hello..! Welcome to Banking Sector..!! ".center(80))

data = {}
global account_no
account_no = 11110

def new_user():
    Username = input("Enter username ")
    mobile_no = input("Enter mobile number ")
    address = input("Enter your address ")
    global account_no 
    account_no+=1    
    while True:
        print("----------------------------------------------------------------------------------------")
        balance = input("Enter amount for opening balance ")
        print("----------------------------------------------------------------------------------------")
        if int(balance) < 10000:
            print("Minimum limit is 10000. Please enter proper amount ")

        else:
            data[Username] = {'UserName':Username, 'Account Number':str(account_no), 'Mobile Number':mobile_no, 'Address':address, 'Account Balance':balance }
            print("Your Account number is {} ".format(account_no))
            break 
        
while True:
    print("----------------------------------------------------------------------------------------")
    print("Press 1 to create new User ")
    print("Press 2 to get existing user ")
    print("Press 3 to remove a User ")
    print("Press 4 to enter account number ")
    print("Press 5 to view balance ")
    print("Press 6 to deposit or withdraw amount ")
    print("Press quit to exit ")
    input_of_user = input()
    print("----------------------------------------------------------------------------------------")
    if input_of_user == 'quit':
        break
    else:
        obj_manager = Manager()
        obj_ATM = ATM()
        if input_of_user == '1':
            obj_manager.add_new_user()
        elif input_of_user == '2':
            obj_manager.get_existing_user()
        elif input_of_user == '3':
            obj_manager.remove_user()
        elif input_of_user == '4':
            obj_ATM.get_account_number()
        elif input_of_user == '5':
            obj_ATM.view_balance()
        elif input_of_user == '6':
            obj_ATM.deposit_withdraw()
        else:
            print("Wrong entry! Please enter from above. ")