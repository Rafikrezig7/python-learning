##RANDOM MODULE
import random
random_integer=random.randint(1,10)
print(random_integer)

my_favorite_number=7 #we keep this in file named test.py
import test
print(test.my_favorite_number) # 7 will be displayed

import random
random_number_0_to_1=random.random() # random number between 0 and 1
print(random_number_0_to_1)

import random
random_float=random.uniform(1,10) # random float between 1 and 10
print(random_float)

#heads or tails
import random
random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==1:
    print("Heads")
else:
    print("Tails")

##LISTS
states_of_america=["Deloware","Pensylvania","New York","Florida"]
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])
print(states_of_america[3])

states_of_america=["Deloware","Pensylvania","New York","Florida"]
states_of_america[0]="Delaware" # we can change the value of list item
states_of_america[1]="Penncylvania"
states_of_america.append("Verginia") # we can add new item to the last eleement in list 
print(states_of_america)

import random
friends = ["Rafik","Sami","Yazid","Imad"]
#solution 1
random_friend=random.choice(friends) # this will select a random friend from the list
print(random_friend) # this will print the index of random friend
#solution 2
random_index=random.randint(0,3)
random_friend=friends[random_index]
print(random_friend)

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
combined_list=[list1,list2]
print(combined_list) # this will print the combined list of list1 and list2

#rock paper scissors game
import random
beats = [2, 0, 1]
user_choice =int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors .\n"))
computer_choice = random.randint(0,2)
if user_choice == computer_choice:
    print("It's a draw!")
elif beats[user_choice] == computer_choice:
    print("You win!")
else:
    print("You lose!")