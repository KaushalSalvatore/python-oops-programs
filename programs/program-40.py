'''
process and thread

A Process is: An independent program in execution.
Each process has:
Own memory
Own resources
Own address space

A Thread is: A lightweight unit of execution inside a process.
✅ Same memory ✅ Same resources
'''
from multiprocessing import Process
import os
import time

def worker(name):
    print(f"Process: {name}")
    print(f"Process ID (PID): {os.getpid()}")
    time.sleep(2)
    print(f"Process {name} finished")

if __name__ == "__main__":
    p1 = Process(target=worker, args=("P1",))
    p2 = Process(target=worker, args=("P2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process completed.")


import threading
import os
import time



def worker(name):
    print(f"Thread: {name}")
    print(f"Running in Process ID: {os.getpid()}")
    print(f"Thread ID: {threading.get_ident()}")
    time.sleep(2)
    print(f"Thread {name} finished")

t1 = threading.Thread(target=worker, args=("T1",))
t2 = threading.Thread(target=worker, args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread completed.")