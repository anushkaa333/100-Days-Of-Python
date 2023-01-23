
import random
import string


def encrypt(user1, key):
    user11 = user1.split()
    lst1 = []
    for i in user11:
        if len(i)<=3:
            ss = i[::-1]
            lst1.append(ss)
        else:
            s1 = random.choices(string.ascii_letters,k=key)
            s2 = i[1:]
            s3 = i[0]
            s4 = random.choices(string.ascii_letters,k=key)
            s = ''.join(s1) + s2 + s3 +  ''.join(s4)
            lst1.append(s)
            #s = ''.join( random.choices(string.ascii_letters,k=key)) + s2 + s3+ ''.join(random.choices(string.ascii_letters,k=key))

    en = ' '.join(lst1)    
    return en
            

def decrypt(user2, key):
    user21 = user2.split()
    lst2 = []
    for i in user21:
        if len(i)<=3:
            zz = i[::-1]
            lst2.append(zz)
        else:
            k = key
            z1 = i[k:-k]
            z2 = z1[-1] + z1[:-1]

            lst2.append(z2)
    de = ' '.join(lst2)
    return de
            





while True:
    print("Encrypt - Decrypt program")
    user = int(input("1. Encrypt  2.Decrypt  3.Quit"))
    if(user==1):
        user1 = input("Enter your message")
        key = int(input("Enter a key to encrypt, either 3 or 4 "))
        while True:
            try:
                
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







# Encrypt - Decrypt program
# 1. Encrypt  2.Decrypt  3.Quit1
# Enter your messageasdf ghjk
# Enter a key to encrypt, either 3 or 4 3
# Encrypted text BcwsdfaksI pLdhjkgMLV
# Encrypt - Decrypt program
# 1. Encrypt  2.Decrypt  3.Quit2
# Enter your message to decryptBcwsdfaksI pLdhjkgMLV
# Enter a key given to encrypt3
# Decrypt text asdf ghjk
# Encrypt - Decrypt program
# 1. Encrypt  2.Decrypt  3.Quit3


