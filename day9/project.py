#ACTION PROJECT

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


auction = []

adding_auction = True
auction_people = 0

print(logo)

while(adding_auction):
    auction_people+=1
    each_people_dictionary = {}
    your_name = input("Enter your name")
    your_bid = int(input("Enter your bid:  "))
    each_people_dictionary["name"] = your_name
    each_people_dictionary["your_bid"] = your_bid
    auction.append(each_people_dictionary)
    if(auction_people>1):
        adding_auction = True if input("Do you want more people to add on auction? Y or N?").lower() == "y" else False

winning_bid=auction[0]["your_bid"]
print(winning_bid)
winning_dict = {}
for i in range(len(auction)):
    if auction[i]["your_bid"]>winning_bid:
        winning_dict["name"] = auction[i]["name"]
        winning_dict["your_bid"] = auction[i]["your_bid"]

print(f'{winning_dict["name"]} is winning bid with {winning_dict["your_bid"]}')

