#!/bin/python37

import os
import sys
import time
import random

def child_process(sleep_time):
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child[{pid}]: I am started. My PID is {pid}. Parent PID is {ppid}.")

    time.sleep(sleep_time)

    exit_status = random.randint(0, 1)
    print(f"Child[{pid}]: I am ended. PID is {pid}. Parent PID is {ppid}.")
    os._exit(exit_status)

def main():
    sleep_time = 5

    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        sleep_time = int(sys.argv[1])

    child_process(sleep_time)

if __name__ == "__main__":
    main()