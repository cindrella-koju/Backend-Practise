import asyncio

async def test():
    asyncio.print_call_graph()
    await asyncio.sleep(4)

async def func1():
    print("Hello from func1")
    # asyncio.print_call_graph() 
    await asyncio.sleep(4)
    return "Func1 ended"
async def main():
    task1 = asyncio.create_task(func1(),name="func1")
    task2 = asyncio.create_task(test(),name='test')


    await task1
    await task2  
    # async with asyncio.TaskGroup() as g:
    #     g.
    #     g.create_task(test(),name='test')

asyncio.run(main())