import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = time.strftime('%H')
print(int(timestamp))

timestamp = time.strftime('%M')
print(int(timestamp))

timestamp = time.strftime('%S')
print(int(timestamp))

# H:\100 Days of Python\Day 11-20>python Day15.py
# 19:01:45
# 19
# 1
# 45
# int before timestamp in print stat will remove the intial zero in number


timestamp = time.strftime('%H:%M:%S')
#print(int(timestamp)) #ValueError: invalid literal for int() with base 10: '19:04:28', We can write print(timestamp)
print(timestamp)

timestamp = time.strftime('%H')
print(timestamp)

timestamp = time.strftime('%M')
print(timestamp)

timestamp = time.strftime('%S')
print(timestamp)


# 19:05:44
# 19
# 05
# 44