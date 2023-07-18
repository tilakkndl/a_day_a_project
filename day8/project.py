logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift, encode_decode_option="encode"):
    letter_position = []
    shited_positoin = []
    encoded_decoded_message = ""
    for i in range(len(message)):
        alphabet_index = alphabet.index(message[i])
        letter_position.append(alphabet_index)
        if encode_decode_option=="encode":
             shited_positoin.append(alphabet_index+shift)
        else:
              shited_positoin.append(alphabet_index-shift)
        encoded_decoded_message += alphabet[shited_positoin[i]]
    return encoded_decoded_message



print(logo)
keep_doing=True
while(keep_doing):
    your_choice = input("Enter 'encode' or 'decode': ").lower()
    your_word = input("Enter the message you want ot encode").lower()
    shift = int(input("Enter the shift: "))
    if(your_choice=="encode"):
        encode(your_word, shift, "encode")
        print(f"Your encoded message is {encode(your_word, shift, your_choice)}")
    elif(your_choice=="decode"):
        encode(your_word, shift, )
        print(f"Your decoded message is {encode(your_word, shift, your_choice)}")
    else:
        print("Enter the correct option i.e. 'encode' or 'decode'")
    keep_doing = True if input("Do you want to continue yes or no?: ").lower() == "yes" else False



