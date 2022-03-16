#Program to add two num without + operator

number1 = int(input("Enter number "))
number2 = int(input("Enter number "))

while number2!=0:
    temp = number1&number2
    number1 = number1^number2
    number2 = temp<<1

print(number1)