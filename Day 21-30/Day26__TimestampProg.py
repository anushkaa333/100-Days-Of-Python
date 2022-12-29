import time

timestamp = time.strftime('%H:%M:%S')
#print(int(timestamp)) #ValueError: invalid literal for int() with base 10: '19:04:28', We can write print(timestamp)
print(timestamp)

Hour = int(time.strftime('%H'))

if 4<=Hour<12:
    print("Good Morning!!! Its", Hour)
elif 12<=Hour<19:
    print("Good Evening!!! Its", Hour)
else:
    print("Good Night!!! Its", Hour)


# 05:23:36
# Good Morning!!! Its 5

