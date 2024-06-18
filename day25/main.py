# with open("/media/tilakkndl/New Volume/py/Days/day25/weather-data.csv") as f:
#     content = f.readlines()
# print(content)


# import csv
# with open("/media/tilakkndl/New Volume/py/Days/day25/weather-data.csv") as f:
#     data = csv.reader(f)
#     temperatures=[]
#     for row in data:
#         print(row)
#         if("temp" != row[0]):
#             temperatures.append(temperatures.append(row[1]))
# print(temperatures)


import pandas
from statistics import mean
# data = pandas.read_csv("/media/tilakkndl/New Volume/py/Days/day25/weather-data.csv")
# print(data["temp"])

# data_dict=data.to_dict()
# print(data_dict)

# temp_list=data["temp"]
# print(mean(temp_list.to_list()))
# print((data["temp"]).max())

# #Get data in row
# print(data[data.day=="Monday"])

# print(data[data.temp == data["temp"].max()])

# monday=data[data.day=="Monday"]
# print(monday.temp)



#Create dataFrames from dic
data_dict = {
    "students": ["santosh", "Tilak", "Samir"],
    "scores": [1, 3 ,4]
}

# data_created=pandas.DataFrame(data_dict)
# data.to_csv("day25/new_data.csv")


data = pandas.read_csv("./day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)
greyCount = len(data[data["Primary Fur Color"]=="Gray"])
print(greyCount)
redCount = len(data[data["Primary Fur Color"]=="Cinnamon"])
print(redCount)
blackCount = len(data[data["Primary Fur Color"]=="Black"])
print(blackCount)

#create dataFrames from dic
squarrel_dict={
    "Flur Color": ["gray", "red", "black"],
    "Count": [greyCount, redCount, blackCount]
}

data_created=pandas.DataFrame(squarrel_dict)
data_created.to_csv("day25/squarrel_count.csv")
