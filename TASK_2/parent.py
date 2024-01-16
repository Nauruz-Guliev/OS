#!/usr/bin/env python3

import os
import sys
import random


def start_child_message(ppid, child_pid):
    print(f"Parent[{ppid}]: I ran children process with {child_pid} child_pid.")


def do_fork():
    new_child = os.fork()
    if new_child < 0:
        return do_fork()
    return new_child


def main():
    n = 5
    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        n = int(sys.argv[1])

    ppid = os.getpid()
    child_pids = []
    is_child = False
    i = 0

    while i < n:
        child_pids.append(do_fork())

        if child_pids[i] == 0:
            is_child = True
            break

        start_child_message(ppid, child_pids[i])
        i += 1

    if not is_child:
        i = 0
        while i < n:
            child_pid, status = os.wait()
            status = int(status / 256)
            print(f"Parent[{ppid}]: Child with PID {child_pid} terminated. Exit Status {status}.")

            if status != 0:
                new_child = do_fork()
                if new_child == 0:
                    is_child = True
                    break

                start_child_message(ppid, new_child)
            else:
                i += 1

    if is_child:
        os.execve('./child.py', ["child", str(random.randint(5, 10))], {})


if __name__ == "__main__":
    main()
