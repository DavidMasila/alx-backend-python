import asyncio 

async def main():
    print("masila")
    await foo()
    print('finished')

async def foo():
    print("mwendwa")
    await asyncio.sleep(1)

asyncio.run(main())