import sys
from collections import deque

f = sys.stdin

n = int(f.readline())
is_stack_list = list(map(int, f.readline().split()))
element_list = list(map(int, f.readline().split()))
element_dq = deque()
for i, is_stack in enumerate(is_stack_list):
    if not is_stack:
        element_dq.append(element_list[i])

m = int(f.readline())
query_list = list(map(int, f.readline().split()))

for q in query_list:
    element_dq.appendleft(q)
    print(element_dq.pop(), end=" ")