#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("/media/tilakkndl/New Volume/py/Days/day24/mail_merge/input/name.txt") as f:
    names = f.read()
    names = names.split()
    print(names)

for name in names:
    with open("/media/tilakkndl/New Volume/py/Days/day24/mail_merge/input/mail.txt") as f:
        mail = f.read()
        mail = mail.replace("[name]", name)
        with open(f"/media/tilakkndl/New Volume/py/Days/day24/mail_merge/output/mail_from_{name}.txt", "w") as fw:
            fw.write(mail)
