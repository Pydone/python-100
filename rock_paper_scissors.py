# import random

# random_integer=random.randint(1,10)
# print(random_integer)

# random_number_0_to_1=random.random()*10
# print(random_number_0_to_1)

# random_float=random.uniform(a=1,b=10)
# print(random_float)

# random_head_or_tails=random.randint(a=0,b=1)
# if random_head_or_tails== 0:
#     print("heads")
# else:
#     print("tails")    

#LISTS

# states_of_america=["delaware","penselvania","hogwards"]
# states_of_america.append("hogwards")

# #adding at the end using append() fuction!!
# states_of_america.extend(["tung tung","larila"])
# states_of_america[0]="newjersey"
# print(states_of_america)


# friend=["aditya","sagar","satyam","amit","dante"]
# random.choice(friend)
# #1 option
# print(random.choice(friend))

# #2d option
# random_friend=random.randint(0,4)
# print(friend[random_friend])

#NESTED LIST
# fruits=["apple","banana","orange","peaches","cherries"]
# vegies=["cabbage","tamato","potato","chilli"]

# dirty_dozen=[fruits,vegies]
# print(dirty_dozen)

#FAINAL PROJECT
import random
rock= '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper=''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors='''  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

user_choice=int(input("what do you choose? type 0 for rock,1 for paper or 2 for scissors "))
#0,1,2
if user_choice>=0 and user_choice <=2:
    print("computer chose:")
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("computer chose " )
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lose!!")
elif user_choice== 0 and computer_choice ==2:    
    print("you win!!")
elif computer_choice==0 and user_choice==2:
    print("you lose!!")    
elif computer_choice>user_choice:
    print("you lose!!")
elif user_choice> computer_choice:
    print("you win!")    
elif computer_choice==user_choice:
    print("its a draw")        
