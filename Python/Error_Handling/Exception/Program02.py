# Create a while loop that increases the counter by one every second.
# -> Start count from 0
# -> Stop while loop when the counter is greater than 500
# -> Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x)

import time

count = 0

def counter_function(counter):
    try:
        while counter < 500:
            time.sleep(1)
            counter+=1
            print(counter)
    except KeyboardInterrupt:
        counter_function(counter)

counter_function(count)
