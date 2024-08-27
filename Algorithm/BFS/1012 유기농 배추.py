"""
아이디어
    이중 for -> graph 값 1이고 미방문 노드면 BFS로 덩어리 개수 세기
BFS 자료구조 -> 그래프, visited [][], queue

"""

import sys
from collections import deque
f = sys.stdin

t = int(f.readline())

for _ in range(t):
    m, n, k = map(int, f.readline().split())
    graph_map = [ [0 for _ in range(m)] for _ in range(n) ]
    for _ in range(k):
        x, y = map(int, f.readline().split())
        graph_map[y][x] = 1
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    def bfs(y, x):
        dq = deque()
        dq.append((y, x))
        visited[y][x] = True

        while dq:
            ey, ex = dq.popleft()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if 0<=nx<m and 0<=ny<n and graph_map[ny][nx] == 1 and (not visited[ny][nx]):
                    dq.append((ny, nx))
                    visited[ny][nx] = True

    cnt = 0
    for j in range(n):
        for i in range(m):
            if graph_map[j][i] == 1 and (not visited[j][i]):
                bfs(j, i)
                cnt += 1
    print(cnt)