# import asyncio 

# async def main():
#     print("masila")
#     await foo()
#     print('finished')

# async def foo():
#     print("mwendwa")
#     await asyncio.sleep(1)

# asyncio.run(main())

from random import random
import asyncio
 
# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # return the result
    return arg * value
 
# main coroutine
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # get results as coroutines are completed
    for coro in asyncio.as_completed(coros):
        # get the result from the next coroutine to complete
        result = await coro
        # report the result
        print(f'>got {result}')
 
# start the asyncio program
asyncio.run(main())