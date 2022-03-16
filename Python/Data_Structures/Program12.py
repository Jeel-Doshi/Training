# Create a simulation program for the Hot Potato Game. You can develop with your ideas. Just take care of the following things:
#  At least one person must be removed from each round.
#  Display name in the console that the user has a hot potato.
#  Each user holds a potato for random seconds between 0.1 to 3.0.
#  Each round starts after 3 seconds of the previous elimination.
#  Each round stops at random seconds between 5 to 20.
#  Display the name of the winner.

import random
import time

players = ['Tom','Jerry','Oggy','Bheem','Nobita','Shinchan','Doremon']


while len(players)-1:

    round_time = random.uniform(5,20)
    time_counter = 0
    
    list_index = 0
    while time_counter < round_time:
        
        print("{} has Potato".format(players[list_index]))        
        hold = random.uniform(0.1,3.0)
        time.sleep(hold)  
        time_counter += hold
        list_index+=1

        if list_index>=len(players):
            list_index = 0

    print("----------------------------------------------\n")
    print("{} is eliminated....!!\n".format(players[list_index-1]))
    players.remove(players[list_index-1]) 
    print("----------------------------------------------\n")

    time.sleep(3)

print("{} won the Game...!!!".format(players[0]).center(50))


