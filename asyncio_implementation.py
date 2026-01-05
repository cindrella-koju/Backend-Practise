# import asyncio
# import time

# async def func1():
#     print("Function 1 started")
#     await asyncio.sleep(5)
#     return f"Function 1 ended, {time.ctime()}"

# async def func2():
#     print("Function 2 started")
#     await asyncio.sleep(7)
#     return f"Function 2 ended, {time.ctime()}"

# async def main():
#     print("Coroutine started at:", time.ctime())

#     try:
#         async with asyncio.TaskGroup() as tg:
#             task1 = tg.create_task(func1())
#             task2 = tg.create_task(
#                 asyncio.wait_for(func2(), timeout=3.0)
#             )

#     except* asyncio.TimeoutError:
#         print("func2 timed out")

#     except* Exception as eg:
#         print("Other error:", eg)

#     else:
#         print("Results:")
#         print(task1.result())
#         print(task2.result())

#     print("Coroutine ended at:", time.ctime())

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import requests
import time
import datetime as datetime
import aiohttp

def extarct_json_data():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()  # convert to JSON
    time.sleep(5)

    sum_val = []
    for val in data[:10]:
        sum_val.append(val["id"])

    return sum_val
    # print("Extraction completed at:",time.ctime(time.time()))
def sumfunc():
    sum_val = extarct_json_data()
    result = sum(sum_val)
    return result

def heave_cal():
    sum_val = 0
    for i in range(100000000):
        sum_val = sum_val+ i
    return sum_val

def extract_date():
    return datetime.datetime.now()

async def extract_json_data_async():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/') as response:
            return await response.text()

    # return data

async def main():
    task1 = asyncio.create_task(extract_json_data_async())

    await task1 
    print(task1)

asyncio.run(main())
# if __name__ == "__main__":
    # startdate = extract_date()
    # print("Whole operation started at:",startdate)

    # print(sumfunc())
    # print(heave_cal())

    # enddate = extract_date()
    # print("Whole operation completed at:",enddate)
    # print("Total time take:",enddate-startdate)
