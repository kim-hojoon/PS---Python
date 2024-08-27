import sys
from collections import deque
f = sys.stdin

n, m = map(int, f.readline().split())

graph = [ [] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, f.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]

def bfs(node):
    dq = deque()
    dq.append(node)
    visited[node] = True
    
    while dq:
        node = dq.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                dq.append(next_node)
                visited[next_node] = True
cnt = 0
for node in range(1, n+1):
    if not visited[node]:
        cnt += 1
        bfs(node)

print(cnt)