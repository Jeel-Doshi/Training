# Program to find common divisor of int in pair

num1 = int(input("Enter num "))
num2 = int(input("Enter num "))

tup =(num1,num2)

for n in range(1,max(tup)):
    if tup[0]%n==0 and tup[1]%n==0:
        div = n

print("Common divisor of {} is {}".format(tup,div))


