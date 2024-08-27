import sys
from collections import deque
f = sys.stdin

n = int(f.readline())
m = int(f.readline())

graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, f.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dq = deque()
    dq.append(start)

    visited = [False for _ in range(n+1)]
    visited[start] = True
    
    cnt = 0
    
    while dq:
        v = dq.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                cnt += 1
                dq.append(neighbor)
    return cnt

print(bfs(1))