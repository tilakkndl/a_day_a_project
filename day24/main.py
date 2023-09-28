# file = open(r"/media/tilakkndl/New Volume/py/Days/day24/my_file.txt")
# content = file.read()
# print(content)
# file.close()

#without close one
with open(r"/media/tilakkndl/New Volume/py/Days/day24/my_file.txt", mode="r") as f:
    content = f.read()
    # f.write("haha")
    print(content)