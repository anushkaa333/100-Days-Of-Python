#******************** I] Write
#If file does not exist, then this will create new file and add respective text in it

# f = open("myfile.txt", 'w')
# f.write("Hello World")
# f.close()

#o/p => Hello World



#If file already exist then this will overwrite the new content and previous content will be deleted
# f1 = open("myfile.txt", 'w')  #w=wt 
# f1.write("Namaste World")
# f1.close()

#o/p => Namaste World


#********************** II] Append

#This will create prev content as it was and will add new at the end

# f = open("myfile.txt", 'a')
# f.write("Hello World")
# f.close()

#o/p => Namaste WorldHello World


#*******************  III] Read 

#If file is in read mode then user cant write in it, it will throw error 

# f = open("myfile.txt", 'r') #r=rt
# f.write("Hello World")
# f.close()

# error -io.UnsupportedOperation: not writable



#If file is in read mode then user read it

# f = open("myfile.txt", 'r')
# text = f.read()
# print(text)
# f.close()




#********************** IV] With keyword => allows us to not write close functionality


with open("myfile.txt", 'rt') as f:
    text = f.read()
    print(text)


# Namaste WorldHello World


