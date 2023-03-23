import time
import asyncio

# III] Run functions simultaneously
# Order of display will be amt of time taken by each function, ascendingly
async def function3():
    a = 1 + 2
    b = 1 * 2
    print("Fun3")
    return a + b


async def function2():
    
    a = 2 + 2
    b = 2 * 2
    c = 2 - 2
    print("Fun2")
    return a + b + c 


async def function1():
    a = 23453 + 243758583
    b = 2 * 2
    c = 2 - 2
    d = 2 /2
    print("Fun1")
    return a + b + c + d


async def main():

    L = await asyncio.gather(
    function1(),
    function2(),
    function3()
    )
    
    print(L)

asyncio.run(main())
# Fun1
# Fun2
# Fun3