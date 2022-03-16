# Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity: O(n)

input_list = [1,0,2,2,0,1,0,1,2,0,0]

onearr, twoarr, zeroarr = [], [], []

for value in input_list:
    if value == 0:
        zeroarr.append(value)
    elif value == 1:
        onearr.append(value)
    else:
        twoarr.append(value)

zeroarr.extend(onearr)
zeroarr.extend(twoarr)

print(zeroarr)

