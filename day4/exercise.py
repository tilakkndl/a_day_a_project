import random

# 4.1 head or tail problem

# coin = random.randint(0, 1)
# if coin == 1:
#     print("HEAD")
# else:
#     print("TAIL")


# 4.2 random name generating from list

# name = input("Enter names seperated by commas:")
# name = name.split(",")
# random_index = random.randint(0, len(name)-1)
# print(name[random_index])


# 4.3 filling in the box
row1 = ['😭', '😭', '😭']
row2 = ['😭', '😭', '😭']
row3 = ['😭', '😭', '😭']
map = [row1, row2, row3]

print(map)

row = int(input("Enter row"))
col = int(input("enter column"))
map[row][col] = '😂'
print(map)