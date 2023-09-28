#CALCULATOR PROJECT

bill_amt=float(input("Enter the bill amt?"))
tip_percent = float(input("Enter the tip percentage 12, 10 or 15?"))
total_people = float(input("Enter no of people"))

bill_with_tip = round(bill_amt+bill_amt*tip_percent/100, 2)
print(type(bill_amt), type(tip_percent), type(total_people), bill_with_tip)

bill_amt_each = round(bill_with_tip/total_people, 2)

bill_amt_each = "{: .2f}".format(bill_amt_each)

print(f"Each share {bill_amt_each}")