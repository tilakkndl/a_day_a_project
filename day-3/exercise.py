#even-odd problem
# num = int(input("Enter a number"))
# if num%2==0:
#     print("Even")
# else:
#     print("ODD")

#BMI2.0
# weight = float(input("Enter your weight in kg"))
# height = float(input("Enter your height in m"))

# BMI=round(weight/(height**2))

# if BMI<18.5:
#     print("UNder weight")
# elif BMI<25:
#     print("Normal weight")
# elif BMI<30:
#     print("OVerweight")
# elif BMI<35:
#     print("Obese")
# else:
#     print("Clinically obese")


#Leap Year problem

# year = int(input("Enter year"))
# if year%4==0 and year%100!=0:
#     print("Leap Year")
# elif year%4==0 and year%100==0 and year%400==0:
#     print("Leap year")
# else:
#     print("Not leap year")


#PIZZA BILLING ProBLEM
# print("Welcome to PIZZA billing")
# size = input("Enter size: S, M, L?")
# add_pep = input("Enter if you want pep? Y or N")
# extra_cheese = input("want cheese? Y or N")

# bill = 0

# if size=="S":
#     bill+=15
#     if add_pep=="Y":
#         bill+=2
# elif size=="M":
#     bill+=20
#     if add_pep=="Y":
#         bill+=3
# elif size == "L":
#     bill+=25
#     if add_pep=="Y":
#         bill+=3


# if extra_cheese=="Y":
#     bill+=1
# print(f"The cost is ${bill}")



#Love calculator

name1 = input("Enter first name:")
name2 = input("Enter another name:")


name = name1+name2
name = name.lower()
count_T=name.count("t")
count_R = name.count("r")
count_U = name.count("u")
count_E=name.count("e")

count_TRUE = count_T+count_R+count_U+count_E

count_L = name.count("l")
count_O = name.count("o")
count_V = name.count("v")

count_LOVE = count_L+count_O+count_E+count_V

LOVE_SCORE = str(count_TRUE)+str(count_LOVE)

print(LOVE_SCORE)