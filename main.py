#Understanding random module with 2 simple projects

import random
r= random.randint(1,10)#generates a random number between 1 to 10
print (r)
random_number = random.random() #Generates a floating point number between 0 to 1. Doesn't need any arguements
print(random_number)
# Project 1: Randomly generate heads or  tails based on the random number generated
number= random.randint(1,2)
if number == 1:
    print("Heads")
else:
    print("Tails")

#project 2: Randomly pick the business card that are put up on the table. Whichever card gets picked up should pay the bill.
list=["Matthew","Supriya","Tom","Jim","Arnold"]
print(random.choice(list))# chooses random name from the list.