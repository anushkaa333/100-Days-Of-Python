def welcome():
    print("W-e-l-c-o-m-e")

print(__name__)

if __name__== "__main__" :
    welcome()

#**** I] If curr file is excuted

#__main__
#W-e-l-c-o-m-e


#***** II] If curr file is executed w/o if statement like below


# def welcome():
#     print("W-e-l-c-o-m-e")

# welcome()


# then call this in Day45.py file then it will execute more than 994 times,
# in order to execute 1 time only we will use upper syntax


#********* III] 
#
# Using "__name___"
# repeatation is avoided

#If "__name__" not used in main file and have called the function in main file at the same time in other file, it will repeat
#If "__name__" not used in main file and have not called the function in main file and in other file, it is called , it won't repeat