import sys
from collections import deque
f = sys.stdin

n = int(f.readline())

queue = deque()

for _ in range(n):
    command = list(map(str, f.readline().split()))
    cmd = command[0]

    if cmd == "push":
        queue.append(int(command[1]))

    elif cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print("-1")

    elif cmd == "size":
        print(len(queue))

    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")

    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print("-1")