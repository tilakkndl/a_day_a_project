# checking = 1
# def adding():
#     checking=2
#     print(checking)
#     # return checking+1
# adding()
# print(checking)

#modifying the global variable
checking = 1
def adding():
    # checking=2
    # print(checking)
    print(checking)
    return checking+1
checking = adding()
print(checking)


#constant 
PI = 3.132897