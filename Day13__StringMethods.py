str = "python java cpp"

print(str.upper()) #PYTHON JAVA CPP
print(str.isupper())  #False
print(str.lower()) #python java cpp
print(str.islower()) #True

print(str.rstrip('a')) #python java cpp
print(str.rstrip('p')) #python java c - for stripping it must be at last 
print(str.replace('java', 'js')) #python js cpp
print(str.split(" ")) #['python', 'java', 'cpp']


print(str.capitalize()) #Python java cpp
print(str.count('a')) #2

print(str.endswith('a cpp'))#true
print(str.endswith('acpp'))#false
print(str.endswith('a cpp', 4, 50))#true
print(str.startswith('pyt')) # True


print(str.find('j')) #7
print(str.find('s')) #-1
print(str.index('j')) #7
#print(str.index('s')) #ValueError: substring not found


print(str.isalnum()) #False
str2="anu"
print(str2.isalpha()) #True

str1 = "anushka009"
print(str1.isalnum()) #True
print(str1.isalpha()) #False

str3="anu\n"
print(str3.isprintable()) #False
print(str3.isalpha()) #False

print(str.isspace())








