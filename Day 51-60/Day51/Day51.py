#******************** I]
# r+ => Both read and write 

# f = open("myfile.txt", "r+")

# f.write("My name is Anushka")

# f.seek(10)

# print(f.tell())
# #10

# data = f.read(3)
# print(data)
# #An

# f.close()


#********************* II]
# a+ => Both read and append 


p = open("myfile.txt1", "a+")

data = p.read(3)
print(data)
#This wont display any result as file pointer is at end due to append fuctionality for this use p.seek(0) to move file pointer at start

p.seek(0)
text = p.read(10)
print(text)
#Anushka
#BE

p.close()
