## You're going to write an interactive calculator!
### -> User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
### -> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
### -> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
### -> If the second input is not '+' or '-', again raise a FormulaError
### -> If the input is valid, perform the calculation and print out the result.
### -> The user is then prompted to provide new input, and so on until the user enters quit


Input : Formula that consists of number, an operator and another number seperated by white space

Output : Required calculation (addition or subtraction) with handled errors

| Input       | Output |
| ------      | ------ |
| 1 + 9       | 10.0   |
| 5 - 4       | 1.0    |
| 2.1 + 3.5   | 5.6    |
| 9 - 12      | -3.0   |


### Create a while loop that increases the counter by one every second.
### -> Start count from 0
### -> Stop while loop when the counter is greater than 500
### -> Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x)


Input  : Counter starting with 0 

Output : Counter value from 0 to 500

| Input  | Output |
| ------ | ------ |
| 0      | 0      |
|        | 1      |
|        | 2      |
|        | .      |
|        | .      |
|        | .      |
|        | .      |
|        | 500    |