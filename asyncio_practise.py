import asyncio

# async def func1():
#     print("Function 1 started")
#     await asyncio.sleep(2)
#     print("Function 1 ended")

# async def func2():
#     print("Function 2 started")
#     await asyncio.sleep(3)
#     print("Function 3 ended")

# with asyncio.Runner() as runner:
#     runner.run(func1())
#     runner.run(func1())

# async def tcp_echo_client(message):
#     reader, writer = await asyncio.open_connection('127.0.0.1',8888)
#     print(f"Send : {message}")
#     writer.write(message.encode())
#     await writer.drain()

#     data = await reader.read(100)
#     print(f"Received: {data.decode()}")
#     print("Close the connection")
#     writer.close()

#     await writer.wait_closed()

# asyncio.run(tcp_echo_client("Hello World"))


# async def waiter(event):
#     print('waiting for it ...')
#     await event.wait()
#     print('... got it!')

# async def restaurant(event):
#     print("Restaurant event is waiting")
#     await event.wait()
#     print("Got restaurant event")

# async def main():
#     # Create an Event object.
#     event = asyncio.Event()

#     # Spawn a Task to wait until 'event' is set.
#     waiter_task = asyncio.create_task(waiter(event))
#     restaurant_task = asyncio.create_task(restaurant(event))
#     # Sleep for 1 second and set the event.
#     await asyncio.sleep(1)
#     event.set()

#     # Wait until the waiter task is finished.
#     await waiter_task

# asyncio.run(main())

# async def create_queue():
#     queue = asyncio.Queue()

#     # Put items in the queue
#     await queue.put("apple")
#     await queue.put("banana")
#     await queue.put("cherry")

#     # Display all items in the queue
#     print("Items in queue:", list(queue._queue))

#     # Optionally, get items one by one
#     while not queue.empty():
#         item = await queue.get()
#         print("Got item:", item)

# asyncio.run(create_queue())


async def create_queue():
    queue = asyncio.Queue()

    # Put items in the queue
    await queue.put("apple")
    await queue.put("banana")
    await queue.put("cherry")

    print("Queue size before removing:", queue.qsize())  # 3

    # Remove items one by one
    item1 = await queue.get()
    print("Removed item:", item1)

    item2 = await queue.get()
    print("Removed item:", item2)

    print("Queue size after removing two items:", queue.qsize())  # 1

    # Remove the last item
    item3 = await queue.get()
    print("Removed item:", item3)

    print("Is the queue empty now?", queue.empty())  # True

asyncio.run(create_queue())
