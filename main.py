#Atbash Cipher

#Create two functions that will accept parameters in the form of a list or a dictionary that will contain the string meant to be encrypted or decrypted.
#one function will encrypt
def encrypt(message_list:list):
    encrypted=""
    for item in message_list:
        for char in item:
            if char.isalpha():
                if char.isupper():
                    encrypted+=chr(155 - ord(char))#for uppercase letters, 'A'+'Z'=155
                elif char.islower():
                    encrypted+=chr(219 - ord(char))#for lowercas letters, 'a'+'z'=219
            else:
                encrypted+=char
    index_item=message_list.index(item)
    message_list[index_item]=encrypted
    return message_list
#the other will decrypt using the Atbash cipher technique.
#to decrypt, I will do the same thing because the sum of a and z remains the same, so I can find one character by using its respective one and viceversa
def decrypt(message_list:list):
    decrypted=''
    for item in message_list:
        for char in item:
            if char.isalpha():
                if char.isupper():
                    decrypted+=chr(155 - ord(char))#for uppercase letters, 'A'+'Z'=155
                elif char.islower():
                    decrypted+=chr(219 - ord(char))#for lowercas letters, 'a'+'z'=219
    index_item=message_list.index(item)
    message_list[index_item]=decrypted
    return message_list


# This should involve both loops and if statements.
def add_encrypted(list:list):
    message= (input(f'enter the message you want to encrypt:')).strip()
    list.append(message)
    return list

def add_decrypted(list:list):
    message= (input('enter the message you want to decrypt: ')).strip()
    list.append(message)
    return list

def print_string(message_list: list): #function to print the new message
    for item in message_list:
        print(item)

#ask the user whether they want to decrypt or encrypt a message
#Accept a string that the program will either encrypt or decrypt.
message_list_encr=[]
message_list_decr=[]
#either call a function to encrypt or to decrypt the string.
while True:
        question=input('would you like to decrypt or encrypt the message? ')
        if question=='encrypt':
            message_list_encr=add_encrypted(message_list_encr)
            message_list_encr=encrypt(message_list_encr)
            #Present the final encrypted string to the user.
            print("here's your message encrypted:")
            print_string(message_list_encr)
            
        elif question=='decrypt':
            message_list_decr=add_decrypted(message_list_decr)
            message_list_decr.append(decrypt(message_list_decr))
            #Present the final decrypted string to the user.
            print("here's your message decrypted:")
            print_string(message_list_decr)

        else:
            print('make sure you type either "encrypt" or "decrypt" ')
            continue
    

#The user must be able to copy that output and run it through the program again to perfectly encrypt or decrypt it multiple times without any mistakes