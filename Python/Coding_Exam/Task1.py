# Finding the sum of all digits of a number until the sum becomes a single digit.
# Samples. 10589=>5 , 121=>4, 99=>9, 10=>1

input_num = 10589

if input_num%9 == 0:
    print(input_num%9 + 9)
else:
    print(input_num%9)