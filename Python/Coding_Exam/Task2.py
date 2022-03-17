# Check if the given number is prime or not

input_number = int(input("Enter any num "))

counter = 0
for number in range(2, input_number):
    
    if input_number % number == 0:
        counter+=1
        break
        

if counter > 0:
    print("Number is not prime")
else:
    print("Number is prime")

