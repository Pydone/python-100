# # print("hello"[-1])
# # # string 
# # print("123"+ "345")
# # # integer= whole number 
# # print(123+345)
# # # large integers
# # print(12_345_67)
# # # float= floating point number
# # print(7.67)
# # # boolean
# # print(True)
# # print(False)

# # type conversion
# # print(int("345")+int("56"))
# # name_of_the_user = input("enter your name: ")
# # length_of_name = len(name_of_the_user)


# # print(type(length_of_name))
# # print(type("number of letters in your name:"))

# # print("number of letters in your name:"+ str(length_of_name))
# print("my age:" + str(12))
# print(123+ 45)
# print(7*7)
# print(5/6)
# print(5//6)
# print(2**3) #square

# print(3*(3+3)/3-3)
# # user scores a point 
# score=0
# score += 1
# print(score)

# # f-strings
# height=1.0
# is_winning= True
# print(f"your score is ={score},your height is = {height},your winning is={is_winning}")
print("welcome to the tip calculator!\n")
bill=float(input("what was the total amount? :\n"))
tip=int(input("what percentage tip would you like to give ? 10, 12, of 15?"))
people= int(input("how many people to split the bill? "))
bill_with_tip = bill* (1 + tip/100)
print(bill_with_tip)
tip_as_percent=tip/100
total_tip_amount= bill*tip_as_percent
total_bill = total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"each person should pay {final_amount}")