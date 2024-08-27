import sys
from collections import deque

f = sys.stdin

n, m, v = map(int, f.readline().split())
graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, f.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    result_dfs.append(v)
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, v, visited):
    dq = deque([v])
    visited[v] = True

    while dq:
        node = dq.popleft()
        result_bfs.append(node)
        for neighbor in sorted(graph[node]):
            if visited[neighbor] == False:
                visited[neighbor] = True
                dq.append(neighbor)

visited = [False for _ in range(n+1)]
result_dfs = []
dfs(graph, v, visited)
print((" ".join(map(str, result_dfs))))

visited = [False for _ in range(n+1)]
result_bfs = []
bfs(graph, v, visited)
print((" ".join(map(str, result_bfs))))