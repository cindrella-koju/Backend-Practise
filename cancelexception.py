import asyncio

async def func1():
    print("Starting the function one")
    await asyncio.sleep(10000)
    print("Function run completed")

async def main():
    try:
        task1 = asyncio.create_task(func1())
        await asyncio.sleep(20)
        task1.cancel()
        await task1
    except asyncio.CancelledError as e:
        print("Cancellation Error",e)
    except asyncio.TimeoutError as e:
        print("Timeout Error",e)

if __name__ == "__main__":
    asyncio.run(main())