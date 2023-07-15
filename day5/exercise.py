#5.1 AVERAGE HEIGHT

# heights = input("Enter height seperated by , : ").split()
# print(heights)
# sum = 0

# for i in range(len(heights)):
#     heights[i] = int(heights[i])

# for height in heights:
#     sum += height
# avg = round(sum/len(heights))
# print(f"Average is {avg}")


#5.2 Highest score
# scores = [1, 3, 4, 4444, 5, 6, 88]
# max_score = scores[0]
# for score in scores:
#     if score>max_score:
#         max_score = score
# print(max_score)


#5.3 ADD even numbers
# sum = 0
# for i in range(0, 101, 2):
#     sum+=i
# print(sum)

#5.4 FIZZBUZZ problem
for i in range(0, 101):
    if i%3 == 0 and i%5==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else: 
        print(i)
    