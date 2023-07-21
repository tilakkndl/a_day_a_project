#CALCULATOR PROJECT

def calcualtor(first_no, operator, second_no):
    if(operator == "+"):
        return first_no+second_no
    elif operator == "-":
        return first_no-second_no
    elif operator == "*":
        return first_no*second_no
    elif operator == "/":
        return first_no/second_no
    elif operator == "%":
        return first_no%second_no
    
keep_calculating = True
no_of_operation = 0
result = 0
while(keep_calculating):
    if(no_of_operation==0):
        first_no = float(input("Enter number: "))
        no_of_operation+=1
    else:
        first_no = result
    print("+\n-\n*\n/\n%\n")
    operator = input("Enter your optin: ")
    second_no = float(input("Enter number: "))
    result = calcualtor(first_no, operator, second_no)
    print(f"The result is : {result}") 
    keep_calculating = True if input("Do you want to contunue? Y or N?").lower()== "y" else False
