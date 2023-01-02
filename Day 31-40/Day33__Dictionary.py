#dictionaries are ordered unlike sets from python 3.7 version

# dict = {key : value}


#************************** I] Strings
dic = {'Ram':80, 'Sita':85, 'Sugriv':90, 'Wali':95}
print(dic['Ram']) #80
print(dic.get('Ram')) #80


# *************************** II] Int 
dic = {1:'Ram', 2:'Sita', 4:'Sugriv', 3:'Wali'}
print(dic)

print(dic[4]) #Sugriv
print(dic.get(3)) #Wali


#********************** III] Print - Key Value Items seperataly

print(dic.keys()) #dict_keys([1, 2, 4, 3])
print(dic.values()) #dict_values(['Ram', 'Sita', 'Sugriv', 'Wali'])
print(dic.items()) #dict_items([(1, 'Ram'), (2, 'Sita'), (4, 'Sugriv'), (3, 'Wali')])


#************************* IV] For loop

for key in dic.keys():
    print(key)
    print(f"Value of key {key} is {dic.get(key)}")
    # 1
    # Value of key 1 is Ram
    # 2
    # Value of key 2 is Sita
    # 4
    # Value of key 4 is Sugriv
    # 3
    # Value of key 3 is Wali


for key, value in dic.items():
    print("Key {} and its value is {}".format(key, value))


# Key 1 and its value is Ram
# Key 2 and its value is Sita
# Key 4 and its value is Sugriv
# Key 3 and its value is Wali