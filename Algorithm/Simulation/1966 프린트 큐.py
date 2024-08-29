import sys
from collections import deque
f = sys.stdin

t = int(f.readline())

for _ in range(t):
    n, m = map(int, f.readline().split())
    dq = deque(list(map(int, f.readline().split())))
    cnt = 0
    while dq:
        key = max(dq)
        e = dq.popleft()
        if m == 0:
            if e == key:
                cnt += 1
                print(cnt)
                break
            else:
                dq.append(e)
                m = len(dq) - 1
        else:
            m -= 1
            if e == key:
                cnt += 1
            else:
                dq.append(e)