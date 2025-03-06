#Atbash Cipher

#Create two functions that will accept parameters in the form of a list or a dictionary that will contain the string meant to be encrypted or decrypted.
#one function will encrypt
def encrypt(message:list):
    encrypted=""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted+=chr(155 - ord(char))#for uppercase letters, 'A'+'Z'=155
            elif char.islower():
                encrypted+=chr(219 - ord(char))#for lowercas letters, 'a'+'z'=219
        else:
            encrypted+=char
    return encrypted
#the other will decrypt using the Atbash cipher technique.
#to decrypt, I will do the same thing because the sum of a and z remains the same, so I can find one character by using its respective one and viceversa
def decrypt(message:list):
    decrypted=''
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted+=chr(155 - ord(char))#for uppercase letters, 'A'+'Z'=155
            elif char.islower():
                encrypted+=chr(219 - ord(char))#for lowercas letters, 'a'+'z'=219

# This should involve both loops and if statements.



#Either call a function to encrypt or to decrypt the string.




#Present the final encrypted or decrypted string to the user.
#The user must be able to copy that output and run it through the program again to perfectly encrypt or decrypt it multiple times without any mistakes