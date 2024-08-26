import sys
import collections

f = sys.stdin
dq = collections.deque()

n = int(f.readline())

for _ in range(n):
    command = list(map(int, f.readline().split()))
    cmd = command[0]

    if cmd == 1:
        dq.appendleft(command[1])
    elif cmd == 2:
        dq.append(command[1])
    elif cmd == 3:
        if dq: print(dq.popleft())
        else: print(-1)
    elif cmd == 4:
        if dq: print(dq.pop())
        else: print(-1)
    elif cmd == 5:
        print(len(dq))
    elif cmd == 6:
        if dq: print(0)
        else: print(1)
    elif cmd == 7:
        if dq: print(dq[0])
        else: print(-1)
    elif cmd == 8:
        if dq: print(dq[-1])
        else: print(-1)