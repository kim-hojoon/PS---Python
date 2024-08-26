# import sys
# f = sys.stdin

# n, k = map(int, f.readline().split())

# num_list = [i for i in range(1,n+1)]

# index = 0

# answer_list = []

# while len(num_list) != 0:
#     index += k-1
#     index = index % len(num_list)
#     answer_list.append(num_list[index])
#     del num_list[index]

# string = ", ".join(map(str, answer_list))

# print(f"<{string}>")

import sys
from collections import deque

f = sys.stdin

n, k = map(int, f.readline().split())
queue = deque(range(1, n+1))

result = []
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft()) 
    result.append(str(queue.popleft()))

print("<" + ", ".join(result) + ">")