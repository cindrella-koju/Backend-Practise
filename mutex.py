import asyncio

shared_counter = 0
lock = asyncio.Lock()

async def func1():
    print("Function 1 attempting to acquire lock")
    global shared_counter
    async with lock:
        print("Function 1 lock acquired")
        await asyncio.sleep(3)
        shared_counter = shared_counter + 1
        print("Function 1 realease the lock")

async def func2():
    print("Function2 attempting to acquire lock")
    global shared_counter
    async with lock:
        print("Function 2 acquire lock")
        await asyncio.sleep(2)
        shared_counter = shared_counter + 1
        print("Function 2 release lock")

async def func3():
    print("Function3 attempting to acquire lock")
    global shared_counter
    async with lock:
        print("Function 3 acquire lock")
        await asyncio.sleep(2)
        shared_counter = shared_counter + 1
        print("Function 3 release lock")

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(func1())
        task1 = tg.create_task(func2())
        task3 = tg.create_task(func3())

    print("Final shared counter value:",shared_counter)

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
