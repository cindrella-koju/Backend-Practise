import asyncio


async def func1(semaphore):
    async with semaphore:
        print("Function 1 acquire semaphore")
        await asyncio.sleep(2)
        print("Function 1 release semaphore")

async def func2(semaphore):
    async with semaphore:
        print("Function 2 acquire semaphore")
        await asyncio.sleep(3)
        print("Function 2 release semaphore")

async def func3(semaphore):
    async with semaphore:
        print("Function 3 acquire semaphore")
        await asyncio.sleep(2)
        print("Function 3 release semaphore")

async def main():
    sm = asyncio.Semaphore(2)
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(func1(sm))
        task2 = tg.create_task(func2(sm))
        task3 = tg.create_task(func3(sm))

    print("All tasks completed")


asyncio.run(main())