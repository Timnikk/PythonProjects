##Create a program that will generate a password. The user can select the length of the password and the password can only contain one of the next characters:
##"qwertyuiopasdfghjklzxcvbnmQWERTTYUIOPASDFGHJKLZXCVBNM1234567890"

import random
len = int(input("Enter the length of your password: "))
char = "qwertyuiopasdfghjklzxcvbnmQWERTTYUIOPASDFGHJKLZXCVBNM1234567890"
n = 1
for n in range(1,len):
    n += 1
    print(random.choice(char),end="")
