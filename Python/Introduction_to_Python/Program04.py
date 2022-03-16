# Program to filter even and odd using lambda

original_list = [1,2,3,4,5,6,7,8,9,10]

even = filter (lambda x: x % 2 == 0, original_list)
print(list(even))

odd = filter (lambda x: x % 2 != 0, original_list)
print(list(odd))