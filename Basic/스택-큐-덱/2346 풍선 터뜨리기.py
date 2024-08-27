import sys
from collections import deque

f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))
dq = list(range(0, n))

result = []
index = 0
while True:
    v = dq[index]
    result.append(v+1)
    dq.remove(v)

    if dq:
        if num_list[v] > 0 :
            index += num_list[v] - 1
            index = index % len(dq)
        else:
            index += num_list[v]
            index = index % len(dq)
    else:
        break

print(" ".join(map(str, result)))