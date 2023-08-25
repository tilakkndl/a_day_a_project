MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

no_of_penny = 0
no_of_dime=0
no_of_nickel = 0
no_of_quarter = 0
machine_money = 0.00
refund_money = 0.00
money_by_user = 0.00
keep_coffeing = True

def take_coffe():
    def calculate_money_by_user(no_of_penny, no_of_dime, no_of_nickel, no_of_quarter):
        return no_of_penny*0.01+no_of_dime*0.1+no_of_nickel*0.05+no_of_quarter*0.25

    def check_money(user_money, coffe_money):
        return user_money>coffe_money

    def check_resources(available_resources, required_resources):
        common_keys = available_resources.keys() and required_resources.keys()
        print(common_keys)
        for key in common_keys:
            if not(available_resources[key]>=required_resources[key]):
                return False
        return True
            

    user_need = input("What do you want? ").lower()

    if(user_need == "off"):
        print("The macine is user MANTAINENCE.")
        exit()

    no_of_penny = int(input("how many penny?"))
    no_of_dime = int(input("How many dime?"))
    no_of_nickel = int(input("How many nickle?"))
    no_of_quarter = int(input("How many quarter?"))

    money_by_user = calculate_money_by_user(no_of_penny, no_of_dime, no_of_nickel, no_of_quarter)

    print(money_by_user)

    if(check_money(money_by_user, MENU[user_need]["cost"])):
        refund_money = (money_by_user-MENU[user_need]["cost"])
        print(f"money is sufficient. So {refund_money} is refunded")

    else:
        print(f"money is insufficient. So {money_by_user} is refunded")
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    # user_need = "latte"
    if(check_resources(resources, MENU[user_need]["ingredients"]) and check_money(money_by_user, MENU[user_need]["cost"])):
        #adding money to coffee machine
        global machine_money
        machine_money += MENU[user_need]["cost"]
        resources["water"] -= MENU[user_need]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_need]["ingredients"]["coffee"]
        resources["milk"] -= MENU[user_need]["ingredients"]["milk"]
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
    elif not check_resources(resources, MENU[user_need]["ingredients"]):
        print("Sorry ! The avaiable resource is not sufficient ")
        
    print(f"The remaining resources are water {water } milk {milk} coffee {coffee} coffee money {machine_money}")

take_coffe()
while(keep_coffeing):
    keep_coffeing = True if input("Want coffe again? [Y/N]: ").lower()=="y" else False
    if(keep_coffeing):
        take_coffe()