import time
import asyncio

# II] Run function semi-simaltaneously
# Next function will start executing if prev function has gone for input/output operation
async def function1():
    await asyncio.sleep(1) 
    print("Fun1")


async def function2():
    await asyncio.sleep(3) 
    print("Fun2")


async def function3():
    await asyncio.sleep(1) 
    print("Fun3")



async def main():

    task = asyncio.create_task(function1())
    # await function1()
    await function2()
    await function3()
    # here first function1 is scheduled and in between this time function2 has started its exexcution

asyncio.run(main())



# here first function1 is scheduled and in between this time function2 has started its exexcution
# Total time = Scheduled time + Execution time
# Hence for Total time(fun1) = Scheduled time + Execution time = 1sec + 1sec = 2sec
# fun2 = 0 + 1 = 1
# fun3 = 0 + 1 = 4



#o/p
# Fun2
# Fun1
# Fun3