#Ex.7

#Rename all jpg files only in a folder.


import os

files = os.listdir("allFiles")
print(files)
# ['applsci-10-04872.pdf', 'pexels-luis-quintero-2148216.jpg', 'pexels-marc-mueller-380768.jpg', 'pexels-rajesh-tp-1633578.jpg']

i=1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"allFiles/{file}", f"allFiles/{i}.jpg") 
        i = i+1
