import time
import asyncio

#********** I] Run all functions one after other -
# Next function wont get executed before prev gets complete
async def function1():
    time.sleep(1) # instead of time.sleep if we use asyncio.sleep, it will throw error
    print("Fun1")


async def function2():
    time.sleep(1)
    print("Fun2")


async def function3():
    time.sleep(4)
    print("Fun3")



async def main():
    await function1()
    await function2()
    await function3()

asyncio.run(main())




#O/P = >
# Fun1
# Fun2
# Fun3