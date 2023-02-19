import os

#***************** I] List folder items

print(os.listdir("data")) #['Data1', 'Data2', 'Data3', 'Data4', 'Data5']


folders = os.listdir("data")

print(type(folders)) #<class 'list'>

for folder in folders:
    print(os.listdir(f"data/{folder}"))


# []
# []
# ['tut.md']
# []
# []



#*********************** II] Chnage directory

print(os.getcwd()) 
# H:\100 Days of Python\Day 41-50\Day46__osModule



# below code displaying error
# os.chdir("/H:")
# print(os.getcwd()) 