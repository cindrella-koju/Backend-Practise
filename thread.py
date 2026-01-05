import threading

# Function to be run in a separate thread (example)
def my_func():
    print(f"Thread '{threading.current_thread().name}' starting...")
    # Simulate work
    import time
    time.sleep(2)
    print(f"Thread '{threading.current_thread().name}' ending...")

# Create and start a new thread
t = threading.Thread(target=my_func, name="WorkerThread")
t.start()

# Enumerate all active threads
print("List of all active threads:")
for thread in threading.enumerate():
    print(f"- Name: {thread.name}, ID: {thread.ident}, Alive: {thread.is_alive()}")

# The list includes the main thread and any other active threads you created.
t.join() # Wait for the worker thread to finish
print("After join, active threads:", threading.active_count()) # Count active threads
