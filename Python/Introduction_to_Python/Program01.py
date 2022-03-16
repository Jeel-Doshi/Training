#Function to determine all num in sequence are unique or not

def diff_num(*x):
    if len(x) == len(set(x)):
        return True
    else:
        return False

print(diff_num(1,2,3,4,2,1))