# Finding the sum of all digits of a number until the sum becomes a single digit.
# Eadditionamples. 10589=>5 , 121=>4, 99=>9, 10=>1

input_num = 10589

def summation(input_num):
    sum = 0

    while input_num > 0 :
        sum = sum + (input_num%10)
        input_num = input_num // 10

    return sum 

addition = summation(input_num)

if addition > 9:
    summation(addition)

print(summation(addition))