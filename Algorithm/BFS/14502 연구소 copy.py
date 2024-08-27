"""
아이디어
- 바이러스 확산 -> BFS로 계산 가능
- 벽을 반드시 3개 세워야 함 -> 벽을 세울 수 있는 모든 경우의 수에 대해 BFS로 영역 계산? for 문
- 3 <= N, M <= 8 이므로 최대 맵 크기 64에 대해 경우의 수는 64C3이므로 크지 않음
"""

import sys
from collections import deque
from itertools import combinations
f = sys.stdin


n, m = map(int, f.readline().split())
graph_map = [ list(map(int, f.readline().split())) for _ in range(n) ]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(graph_map):
    dq = deque()

    for j in range(n):
        for i in range(m):
            if graph_map[j][i] == 2:
                dq.append((j, i))

    while dq:
        ey, ex = dq.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if (0<=nx<m) and (0<=ny<n) and (graph_map[ny][nx] == 0):
                graph_map[ny][nx] = 2
                dq.append((ny, nx))

    safe_area = sum(row.count(0) for row in graph_map)
    return safe_area

empty_spaces = [(y, x) for y in range(n) for x in range(m) if graph_map[y][x] == 0]
max_area = 0

for walls in combinations(empty_spaces, 3):
    new_map = [row[:] for row in graph_map]
    for y, x in walls:
        new_map[y][x] = 1

    safe_area = bfs(new_map)
    max_area = max(max_area, safe_area)

print(max_area)