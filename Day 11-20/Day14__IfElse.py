
#conditional opeartors
# < , > , <= , >= , == , !=



price = int(input("Enter price"))

if(price<70):
    print("Front Seats")
else:
    if(70<price<100):
        print("2D Silver")
    elif(price>110):
        print("2D Gold")
    elif(price>150):
        print("3D Silver")
    elif(price>200):
        print("3D Gold")
    else:
        print("Balcony")


# Enter price80
# 2D Silver

# Enter price250
# 2D Gold


price = int(input("Enter price"))

if(price<70):
    print("Front Seats")
else:
    if(70<price<100):
        print("2D Silver")
    elif(100<=price<150):
        print("2D Gold")
    elif(150<=price<200):
        print("3D Silver")
    elif(200<=price<250):
        print("3D Gold")
    else:
        print("Balcony")


# Enter price120
# 2D Gold


# Enter price240
# 3D Gold