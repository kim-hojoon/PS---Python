"""
아이디어 - BFS로 확장해나가며 k에 닿을 때까지 진행
1중 for문 => O(n-k) => 10^5
"""

import sys
from collections import deque
f = sys.stdin

n, k = map(int, f.readline().split())

bound = 100000

graph = [0 for _ in range(bound + 1)]

dq = deque()
dq.append(n)

def bfs():
    while dq:
        x = dq.popleft()
        if x == k:
            return graph[x]
        for nx in [x-1, x+1, 2*x]:
            if 0<=nx<=bound and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                dq.append(nx)
    
print(bfs())