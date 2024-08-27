"""
아이디어
이중 for 문 - BFS의 1로 시작해서 해당 토마토가 익게 되는 날짜로 update 그리고 max 값을 return
"""

import sys
from collections import deque
f = sys.stdin

m, n = map(int, f.readline().split())

graph = [ list(map(int, f.readline().split())) for _ in range(n) ]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(start_list):
    visited = [[False for _ in range(m)] for _ in range(n)]

    dq = deque()
    for (y, x) in start_list:
        dq.append((y, x))
        visited[y][x] = True

    while dq:
        ey, ex = dq.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=nx<m and 0<=ny<n and (graph[ny][nx] not in [-1, 1]) and not visited[ny][nx]:
                dq.append((ny, nx))
                visited[ny][nx] = True
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[ey][ex] + 1
                else:
                    graph[ny][nx] = min(graph[ny][nx], graph[ey][ex] + 1)

start_list = []
for j in range(n):
    for i in range(m):
        if (graph[j][i] == 1):
            start_list.append((j, i))
bfs(start_list)

maxv = 0
for row in graph:
    if 0 in row:
        maxv = 0
        break
    else:
        maxv = max(maxv, max(row))

print(maxv-1)