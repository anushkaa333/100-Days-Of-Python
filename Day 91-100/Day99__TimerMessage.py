import time
from plyer import notification

t  = int(input("After how many secs it should notify"))

while True:
    time.sleep(t)
    notification.notify(title = "Water", message= "Drink water", timeout=2)




# t  = int(input("After how many hours it should notify"))

# while True:
#     time.sleep(3600 * t)
#     notification.notify(title = "Water", message= "Drink water", timeout=2)
