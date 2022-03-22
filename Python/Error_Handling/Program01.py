# You're going to write an interactive calculator!
# -> User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
# -> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# -> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# -> If the second input is not '+' or '-', again raise a FormulaError
# -> If the input is valid, perform the calculation and print out the result.
# -> The user is then prompted to provide new input, and so on until the user enters quit

class FormulaError(Exception):

    def __init__(self, value):
        self.value = value
 
    def __str__(self):
        return(repr(self.value))

while True:

    user_input = input("Enter formula seperated by white space or quit to exit ").split()
    
    if "".join(user_input) == 'quit':
        break
    
    else:
        try :
            if len(user_input) != 3:
                raise FormulaError(user_input)
            
            if user_input[1] != '+' and user_input[1] != '-':
                raise FormulaError(user_input[1])


            float_input1 = float(user_input[0])
            float_input2 = float(user_input[2])
    
            if user_input[1] == '+':
                result = float_input1 + float_input2
                print(result)
            elif user_input[1] == '-':
                result = float_input1 - float_input2
                print(result)

            
        except ValueError as err:
            raise FormulaError("FormulaError Occured ") from err
            
        except FormulaError:
            print("FormulaError Occured ")


    
