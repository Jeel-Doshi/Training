### Take the word and its meaning as input from the user.
### -> Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
### -> Now use the __str__() function to return a string that contains the word and meaning.
### -> Store the returned strings in a list named flash.
### -> Use a while loop to print all the stored flashcards.
### -> Add proper error handling


Input  : Word and its meaning

Output : All flashcards added by user 

| Input       | Output                    |
| ------      | ------                    |
| gm          | gm (good morning)         |
| ttyl        | ttyl (talk to you later)  |



### Create classes according to the following class-map:
### Animal => Wild => Leopard, Tiger
### => Pet => Dog
### => Canine => Fox
### => Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
### For example,
### print(dog.get_name())  ⇒ My name is Tommy
### print(dog.get_info())  ⇒ I am Dog. I am Pet. I am Animal



Input : Access class method with class name 

Output : Name of class and information of hierarchy 

| Input                     | Output                            |
| ------                    | ------                            |
| print(Tiger.get_name())   | Hello..! My name is Lion          |
| print(Tiger.get_info())   | I am Tiger I am wild I am Animal  |



### Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades) and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
### -> Create a class deck. That contains a method to get a card set containing 52 elements.
### -> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.
### -> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. Total points of both players and display name of winner player


Input : Any two integers

Output : Common divisor of two number (HCF)

| Input      | Output                             |
| ------     | ------                             |
| player-1   |                                    |
| player-2   |                                    |
|            | Winner is Player-1 with 138 points |


### Create a class for Users :
### Username
### account no
### mobile no
### Address
### account balance
### -> Create a class for user manager
###     Manages user => Add new user, Get existing user, remove user
### -> Create a class for ATM,
### -> Enter account no and get user if not found then show a valid message
### -> Show options for user operations like creating new users, View Balance, Deposit, Withdraw, Close account, etc...
### -> Transaction charge: 0.5 for every operation
### -> Account balance limit: 10000


Input  : Number to perform operation

Output : Details of operation performed

```sh
Hello..! Welcome to Banking Sector..!!                      
----------------------------------------------------------------------------------------
Press 1 to create new User 
Press 2 to get existing user 
Press 3 to remove a User 
Press 4 to enter account number 
Press 5 to view balance 
Press 6 to deposit or withdraw amount 
Press quit to exit 
1
----------------------------------------------------------------------------------------
Enter username Tom
Enter mobile number 9879879879
Enter your address Rajkot
----------------------------------------------------------------------------------------
Enter amount for opening balance 12000
----------------------------------------------------------------------------------------
Your Account number is 11111 
Welcome..! You are now the user of the Bank..! 
----------------------------------------------------------------------------------------
Press 1 to create new User 
Press 2 to get existing user 
Press 3 to remove a User 
Press 4 to enter account number 
Press 5 to view balance 
Press 6 to deposit or withdraw amount 
Press quit to exit 
2
----------------------------------------------------------------------------------------
Existing users are as follows: 
Tom

----------------------------------------------------------------------------------------
Press 1 to create new User 
Press 2 to get existing user 
Press 3 to remove a User 
Press 4 to enter account number 
Press 5 to view balance 
Press 6 to deposit or withdraw amount 
Press quit to exit 
4
----------------------------------------------------------------------------------------
Enter account number 11111
Your current balance is 12000 
----------------------------------------------------------------------------------------
Press 1 to create new User 
Press 2 to get existing user 
Press 3 to remove a User 
Press 4 to enter account number 
Press 5 to view balance 
Press 6 to deposit or withdraw amount 
Press quit to exit
quit
```

### Create class Person:
### - Name
### - DOB
### - City
### - Contact No
### Create class Employee (Inherit person class)
### - employee id
### - joining date
### - salary
### - department
### - post
### Employee manager class
### - Add/Remove Employee, Get all employees list, get employee by his name, get all employees by his/her department
### Task:
### 1. Add a few employees
### 2. Print all the employees
### 3. Find an employee with the name
### 4. Print all employees with department Finance
### 5. Find all employees whose salary is greater than 50000
### 6. Find all employees whose salary is between 50000-100000
### 7. Find a list of employees who are joined in the current year
### 8. Find all employees who are from Mirzapur
### 9. Find employees whose birthday in the current month
### 10. Find employees whose age is less than 30.

Input and Output :

```sh
---------------------------------------
Press 1 to create new employee 
Press 2 to remove employee 
Press 3 to get list of all employee 
Press 4 to get employee by name 
Press 5 to get employee by department 
Press 6 to get employee by salary above or salary range 
Press 7 to get employee who joined current year 
Press 8 to get employee by city 
Press 9 to get employee whose birthday is in current month 
Press 0 to get employee by age 
Press quit to exit 
1
---------------------------------------
Enter name of employee - Tom
Enter date of birth seperated with '/' in dd/mm/yy format - 03/04/1998
Enter city - Mumbai
Enter contact number - 9999999999
Enter employee id - tom123
Enter date of joining seperated with '/' in dd/mm/yyyy format - 07/01/2022
Enter salary of employee - 5000
Enter department - Finance
Enter post of employee - Accountant
---------------------------------------
New employee successfully added..! 
---------------------------------------
Press 1 to create new employee 
Press 2 to remove employee 
Press 3 to get list of all employee 
Press 4 to get employee by name 
Press 5 to get employee by department 
Press 6 to get employee by salary above or salary range 
Press 7 to get employee who joined current year 
Press 8 to get employee by city 
Press 9 to get employee whose birthday is in current month 
Press 0 to get employee by age 
Press quit to exit 
quit
---------------------------------------
```
