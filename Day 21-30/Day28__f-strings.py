
name = "Anushka"
country = "India"


#******************* I] F in string 

str = f"My name is {name} and Im from {country}"
print(str) #My name is Anushka and Im from India

#***************** II] Format

str = "My name is {} and Im from {}"
print(str.format(name, country)) #My name is Anushka and Im from India


str = "Im from {1} and  My name is {0} " #place 1 and 0 only, not 2 and 1
print(str.format(name, country)) #Im from India and  My name is Anushka 


#******************** III] .2f

price = 49.985432
str1 = f" Price is {price:.2f}"
print(str1) # Price is 49.99

#******************** IV] Display variables as they are

str = f"My name is {{name}} and Im from {{country}}"
print(str)
#My name is {name} and Im from {country}
