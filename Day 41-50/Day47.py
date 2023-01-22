

import random
import string


def encrypt(user1, key):
    user11 = user1.split(" ")
    for i in user11:
        if len(i)<=3:
            s = i[::-1]
        else:
            s1 = random.choices(string.ascii_letters,key)
            s2 = i[1:]
            s3 = i[0]
            s4 = random.choices(string.ascii_letters,key)
            s = s1 + s2 + s3+ s4
            return s
            


while True:
    print("Encrypt - Decrypt program")
    user = int(input("1. Encrypt  2.Decrypt  3.Quit"))
    if(user==1):
        user1 = input("Enter your message")
        
        while True:
            try:
                key = int(input("Enter a key to encrypt"))
                if (key<0 or key>0):
                    break
            except Exception as e:
                print("Enter only digits")
            
        ans1 = encrypt(user1, key)
        print(f"Encrypted text {ans1}")

    if(user==2):
        user2 = input("Enter your message to decrypt")
        
        while True:
            try:
                key = int(input("Enter a key given to encrypt"))
                if (key<0 or key>0):
                    break
            except Exception as e:
                print("Enter only digits")
            
        ans2 = decrypt(user2, key)
        print(f"Decrypt text {ans2}")


    if (user == 3):
        break










