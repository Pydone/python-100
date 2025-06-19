# fruits=["apple","banana","pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+"pie")

# print(fruits)


#sum is used to sum all of the number in the given list...
# sum=0
# for score in student_scores:
#     sum == score

# print(sum)

#max picks up greatest number in the given list

# student_scores=[54,78,89,67,34,68,99]
# max_score =0
# for score in student_scores:
#     if score > max_score:
#         max_score =score
# print(max_score)        
# print(max(student_scores))

#RANGE FUNCTION

#add another comma and type the number it  will skip the 'x' number you entered


# total=0
# for number in range (1,101):
#     total +=number
# print(total)    
import random
latters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','$','&','*','(',')']

print("welcom to the pypassword generator!")
nr_letters=int(input("how many would you like to have in your password? \n"))
nr_symbols=int(input(f"how many symbols would you like?  \n"))
nr_numbers=int(input(f"how many numbers would you like? \n"))

password_letters=[random.choice(latters)for _ in range(nr_letters)]
password_symbols=[random.choice(symbols)for _ in range(nr_symbols)]
password_numbers=[random.choice(numbers)for _ in range(nr_numbers)]

password_list= password_letters +password_numbers+ password_symbols

random.shuffle(password_list)

password= ''.join(password_list) 

print("\n your strong password is:\n "+ password)


