# import sys

# f = sys.stdin

# n = int(f.readline())

# stack = [i for i in range(n,0,-1)]

# while len(stack) != 1:
#     if len(stack) % 2 == 1:
#         del stack[0::2]
#         stack.insert(0, stack.pop())
#     else:
#         del stack[1::2]
# print(stack[0])

import sys
from collections import deque
f = sys.stdin

n = int(f.readline())

q = deque([i for i in range(1, n+1)])

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])