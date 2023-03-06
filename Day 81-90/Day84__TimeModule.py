import time

def w():
    i = 0 
    while (i<5):
        i = i + 1
        
    print("Value of i ", i)

def if_else():
    a = 16
    if (a >= 18):
        print("Voter")
    else:
        print("Not eligible ") 


t1 = time.time()
w()
final_t1 = time.time() - t1
print(final_t1)
# 0.0004467964172363281


t2 = time.time()
if_else()
print(time.time() - t2)
print(final_t2)

# 0.0