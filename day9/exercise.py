# #9.1 
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# def grade_calulation(marks):
#     if(marks>90):
#         return "A+"
#     elif(marks>80):
#         return "A"
#     elif(marks>70):
#         return "B+"
#     elif(marks>60):
#         return "B"
#     elif(marks>50):
#         return "C+"
#     elif(marks>40):
#         return "C"
#     elif(marks>35):
#         return "D+"
#     else:
#         return "Fail"

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     student_grades[student] = grade_calulation(student_scores[student])

    

# # 🚨 Don't change the code below 👇
# print(student_grades)


#9.2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
    newDic = {}
    newDic[country] = country
    newDic[visits] = visits
    newDic["cities"] = cities
    travel_log.append(newDic)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)









