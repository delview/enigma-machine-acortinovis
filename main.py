#Atbash Cipher

#Create two functions that will accept parameters in the form of a list or a dictionary that will contain the string meant to be encrypted or decrypted.
#one function will encrypt using the Atbash cipher technique.
def encrypt(message_list:list):
    encrypted=""
    for item in message_list:
        for char in item:
            if char.isalpha():
                if char.isupper():
                    encrypted+=chr(155 - ord(char))#for uppercase letters, 'A'+'Z'=155
                elif char.islower():
                    encrypted+=chr(219 - ord(char))#for lowercase letters, 'a'+'z'=219
            else:
                encrypted+=char
    index_item=message_list.index(item) #to find the string position in the list and then replace it
    message_list[index_item]=encrypted
    return message_list #return the list that now contains the encrypted message and not the original message anymore
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
                    decrypted+=chr(219 - ord(char))#for lowercase letters, 'a'+'z'=219
    index_item=message_list.index(item) #to find the string position in the list and then replace it
    message_list[index_item]=decrypted
    return message_list  #return the list that now contains the decrypted message and not the original message anymore

#two functions to add the message the user wants to decrypt/encrypt to the list, which will be used as parameter for the first two functions
def add_encrypt(list:list):
    message= (input(f'enter the message you want to encrypt: ')).strip()
    list.append(message)
    return list

def add_decrypt(list:list):
    message= (input('enter the message you want to decrypt: ')).strip()
    list.append(message)
    return list
#function to print the new message
def print_string(message_list: list): 
    for item in message_list:
        print(item)

#ask the user whether they want to decrypt or encrypt a message
#Accept a string that the program will either encrypt or decrypt.

#either call a function to encrypt or to decrypt the string.
while True:
    message_list_encr=[]
    message_list_decr=[]
    question=input('would you like to decrypt or encrypt the message? ')
    if question=='encrypt':
        message_list_encr=add_encrypt(message_list_encr) #to add the string they want to encrypt to the list
        message_list_encr=encrypt(message_list_encr) #to add to the list the encrypted string intead of the one entered by the user
        #Present the final encrypted string to the user.
        print("here's your message encrypted:")
        print_string(message_list_encr) #call function to print the encrypted sring
        
    elif question=='decrypt':
        message_list_decr=add_decrypt(message_list_decr) #to add the string they want to decrypt to the list
        message_list_decr=decrypt(message_list_decr) #to add to the list the decrypted strin intead of the one entered by the user
        #Present the final decrypted string to the user.
        print("here's your message decrypted:")
        print_string(message_list_decr) #call function to print the decrypted sring

    else:
        print('make sure you type either "encrypt" or "decrypt" ')
        continue
    #The user must be able to copy that output and run it through the program again to perfectly encrypt or decrypt it multiple times without any mistakes
    while True:
        again=input('would you like to encrypt or decrypt further this string?(y/n) ')
        if again=='y':
            break
        elif again=="n":
            print('Goodbye!')
            exit()
        else:
            print('make sure your anwer is either "y" or "n" ')
            continue

