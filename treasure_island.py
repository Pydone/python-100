
#project2

# print("welcome to pizza deliveries!")
# bill=0
# size=input("what size of pizza you want? S, M or L :")
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# elif size == "l":
#     bill+= 25
# else:
#     print("your input is invalid!!")    
# pepperoni =input("do you want pepperoni on your pizza? Y or N: ")
# if pepperoni=="y":
#    if size == "s":
#     bill+=2
# else:
#     bill=+3    
# extra_cheese=input("do you want extra cheese? Y or N ?")
# if extra_cheese== "y":
#         bill+=1

# print(f"your final bill is: ${bill}")
#real one
print("welcome to treasure island!!")
print("your mission is to find the treasure.")
user_data=input(("you are at a cross road.where do you want to go? \n Type left or right?? ")).lower()
if user_data == "left":
    print("you've come to a lake. there is an island in middle of the lake.")
    user_data_2=input("do you want to 'swim' to the island or 'wait' for the boat? \n").lower()
    if user_data_2=="wait":
        print("boat has arrived.. will be on island shortly!!")
        user_data_3=input("you've arrived the island!!! Which door you wanna choose? \n 'red','yellow' or 'blue'?").lower()
        if   user_data_3=="red":
            print("so close!! GAME OVER!!")
        elif user_data_3=="yellow":
            print("not a great choice!!GAME OVER!!")
        else:
            print("YOU WIN!!")                
    else:
        print("you've eaten by the sea monster!! Game over!!")    
elif user_data == "right":
    print("fire wall got you!! game over!!")
else :
    print("invalid input !!")         