# Create class Person:
# - Name
# - DOB
# - City
# - Contact No
# Create class Employee (Inherit person class)
# - employee id
# - joining date
# - salary
# - department
# - post
# Employee manager class
# - Add/Remove Employee, Get all employees list, get employee by his name, get all employees by his/her department,
# Task:
# 1. Add a few employees
# 2. Print all the employees
# 3. Find an employee with the name
# 4. Print all employees with department Finance
# 5. Find all employees whose salary is greater than 50000
# 6. Find all employees whose salary is between 50000-100000
# 7. Find a list of employees who are joined in the current year
# 8. Find all employees who are from Mirzapur
# 9. Find employees whose birthday in the current month
# 10. Find employees whose age is less than 30.

from datetime import date
current = date.today()
current_year = str(current.year)
current_month = str(current.month)

class Person:

    def __init__(self,name,dob,city,contact_no):
        self.name = name
        self.dob = dob
        self.city = city
        self.contact_no = contact_no

class Employee(Person):

    def __init__(self,name,dob,city,contact_no,employee_id,joining_date,salary,department,post):
        self.employee_id = employee_id
        self.joining_date = joining_date
        self.salary = salary
        self.department = department
        self.post = post
        super().__init__(name,dob,city,contact_no)
    
data = []
def user_input():
    name = input("Enter name of employee - ")
    dob = input("Enter date of birth seperated with '/' in dd/mm/yy format - ")
    city = input("Enter city - ")
    contact_no = input("Enter contact number - ")
    employee_id = input("Enter employee id - ")
    joining_date = input("Enter date of joining seperated with '/' in dd/mm/yyyy format - ")
    salary = input("Enter salary of employee - ")
    department = input("Enter department - ")
    post = input("Enter post of employee - ")
    print("---------------------------------------")
    
    global obj_Employee
    obj_Employee = Employee(name,dob,city,contact_no,employee_id,joining_date,salary,department,post)
    data.append(obj_Employee)

class employee_manager:

        def add_employee(self):
            user_input()
            return "New employee successfully added..! "

        def remove_employee(self):
            remove_employee = input("Enter the name of employee to remove ")
            for object in data:
                if remove_employee in object.name:
                    data.remove(object) 
                    return "Employee removed successfully..! "
                else:
                    return "No Employee present "

        def all_employee_list(self):
            print("List of all employees are as follows: ")
            for object in data:
                print(object.name)
            print()

        def employee_by_name(self):
            employee_name = input("Enter the name of employee ")
            for object in data:
                if employee_name in object.name:
                    print("Name {}\nDob {}\nCity {}\nConatact No {}\nEmployee Id {}".format(object.name,object.dob,object.city,object.contact_no,object.employee_id))
                else:
                    print("No employee with name {} is present ".format(employee_name))

        def employee_by_department(self):
            employee_department = input("Enter department to find employee ")
            for object in data:
                if employee_department == object.department:
                    print(object.name)
        
        def employee_salary(self):
            try:
                salary_above = int(input("Enter amount to find employees with salary above "))             
                if salary_above:
                    for object in data:
                        if int(object.salary) > salary_above :
                            print(object.name)
                                
                else:
                    salary_range1 = int(input("Enter lower range of amount "))
                    salary_range2 = int(input("Enter upper range of amount "))
                    for object in data:
                        if salary_range1 < int(object.salary) < salary_range2:
                            print(object.name)

            except ValueError:
                print("ValueError occurred and handled ")

        def joined_current_year(self):
            for object in data:
                year = object.joining_date.split('/')
                if len(year) != 3:
                    print("You entered date in wrong format ")
                else:
                    if year[-1] == current_year:
                        print(object.name)
                    

        def employee_city(self):
            employee_by_city = input("Enter city to find employees ")
            print(employee_by_city)
                
            for object in data:
                if object.city == employee_by_city:
                    print(object.name)
            
            

        def current_bday_month(self):
            for object in data:
                month = object.dob.split('/')
                if len(month) != 3:
                    print("You entered date in wrong format ")
                else:
                    if int(month[1]) == current_month:
                        print(f"{object.name}'s birthday is in current month ")
                    
        
        def employee_by_age(self):
            limit = input("Enter limit of age to get employee whose age is under given age ")
            for object in data:
                year = object.dob.split('/')
                if len(year) != 3:
                    print("You entered date in wrong format ")
                else:
                    age = int(current_year) - int(year[-1])
                    if age < int(limit):
                        print(object.name)

while True:
    print("---------------------------------------")
    print("Press 1 to create new employee ")
    print("Press 2 to remove employee ")
    print("Press 3 to get list of all employee ")
    print("Press 4 to get employee by name ")
    print("Press 5 to get employee by department ")
    print("Press 6 to get employee by salary above or salary range ")
    print("Press 7 to get employee who joined current year ")
    print("Press 8 to get employee by city ")
    print("Press 9 to get employee whose birthday is in current month ")
    print("Press 0 to get employee by age ")
    print("Press quit to exit ")
    input_of_user = input()
    print("---------------------------------------")

    if input_of_user == 'quit':
        break
    else:
        obj_manager = employee_manager()
        match input_of_user:
            case '1':
                print(obj_manager.add_employee())
            case '2':
                print(obj_manager.remove_employee())
            case '3':
                obj_manager.all_employee_list()
            case '4':
                obj_manager.employee_by_name()
            case '5':
                obj_manager.employee_by_department()
            case '6':
                obj_manager.employee_salary()
            case '7':
                obj_manager.joined_current_year()
            case '8':
                obj_manager.employee_city()     
            case '9':
                obj_manager.current_bday_month()
            case '0':
                obj_manager.employee_by_age()          
            case _:
                print("Wrong entry! Please enter from above. ")

    # if input_of_user == 'quit':
    #     break
    # else:
    #     obj_manager = employee_manager()
    #     if input_of_user == '1':
    #         print(obj_manager.add_employee())
    #     elif input_of_user == '2':
    #         print(obj_manager.remove_employee())
    #     elif input_of_user == '3':
    #         obj_manager.all_employee_list()
    #     elif input_of_user == '4':
    #         obj_manager.employee_by_name()
    #     elif input_of_user == '5':
    #         obj_manager.employee_by_department()
    #     elif input_of_user == '6':
    #         obj_manager.employee_salary()
    #     elif input_of_user == '7':
    #         obj_manager.joined_current_year()
    #     elif input_of_user == '8':
    #         obj_manager.employee_city()     
    #     elif input_of_user == '9':
    #         obj_manager.current_bday_month()
    #     elif input_of_user == '0':
    #         obj_manager.employee_by_age()          
    #     else:
    #         print("Wrong entry! Please enter from above. ")
