import requests
import time
import asyncio
import aiohttp
import threading
from concurrent.futures import ThreadPoolExecutor

"""For single API"""

# url = "https://jsonplaceholder.typicode.com/todos"

def sync_fetch(url):
    response = requests.get(url)
    # time.sleep(2)
    return response.json()

# def sync_main():
#     starttime = time.time()
#     result = sync_fetch(url)

#     total = time.time() - starttime
#     print(f"Sync request took {total:.3f} seconds")

async def async_fetch(session, url):
    """With context manager"""
    # async with session.get(url) as response:
    #     await asyncio.sleep(2)
    #     return await response.json()
    
    """Without context manager"""
    try:
        response = await session.get(url)
        # print("REsponse:",response.text  )
        await asyncio.sleep(2)
        return await response.json()
    except Exception as e:
        print("Error occured at async fetch",e)
    finally:
        response.close()
    
# async def async_main():
#     starttime = time.time()

#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         task = asyncio.create_task(async_fetch(session,url))

#         await task
#         # task = await async_fetch(session,url)

#     total = time.time() - starttime
#     print(f"ASync request took {total:.3f} seconds")


"""For multiple API"""

urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
] 

def sync_main():
    starttime = time.time()

    result = [sync_fetch(url) for url in urls]

    total = time.time() - starttime
    print(f"Sync request took {total:.3f} seconds")

"""With context manager"""
# async def async_main():
#     starttime = time.time()

#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         tasks = [async_fetch(session,url) for url in urls]

#         result = await asyncio.gather(*tasks)

#     total = time.time() - starttime
#     print(f"ASync request took {total:.3f} seconds")
def heavy_calculation():
    print(f"Started heavy_calculation  in thread {threading.current_thread().name}")
    total = 0
    for i in range(10000000):
        total += i
    print(f"Finished heavy_calculation")
    return total


def display_threads():
    print("\nActive Threads:")
    for t in threading.enumerate():
        print(f"  {t.name} (id={t.ident})")


async def monitor_threads():
    while True:
        display_threads()
        await asyncio.sleep(2)

"""Without context manager"""
# async def async_main():
#     starttime = time.time()
#     loop = asyncio.get_running_loop()
#     try:
#         session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
#         tasks = [async_fetch(session,url) for url in urls]
#         task = loop.run_in_executor(None,heavy_calculation)
#         result = await asyncio.gather(*tasks,task)
#     except Exception as e:
#         print("Error occurred",e)
#     finally:
#         await session.close()
    
#     total = time.time() - starttime
#     print(f"ASync request took {total:.3f} seconds")

"""For multi threading"""
async def async_main():
    starttime = time.time()
    loop = asyncio.get_running_loop()

    executor = ThreadPoolExecutor(max_workers=1)

    try:
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            tasks = [async_fetch(session, url) for url in urls]

            calc_task = loop.run_in_executor(executor, heavy_calculation)

            result = await asyncio.gather(*tasks, calc_task)

    except Exception as e:
        print("Error occurred", e)

    finally:
        executor.shutdown(wait=True)

    total = time.time() - starttime
    print(f"Async request took {total:.3f} seconds")

async def main():
    await asyncio.gather(
        async_main(),
        monitor_threads(),
    )


if __name__ == "__main__":
    asyncio.run(main())
# if __name__ == "__main__":
#     sync_main()
#     with asyncio.Runner() as runner:
#         runner.run(async_main())
#         runner.run(run_function())
    

