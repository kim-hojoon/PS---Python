import sys
from collections import deque
f = sys.stdin

n, m = map(int, f.readline().split())

graph_map = []
for _ in range(n):
    str_list= list(str(f.readline().strip()))
    temp_list = list(map(int, str_list))
    graph_map.append(temp_list)

distance_map = [[0 for _ in range(m)] for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(start):
    x, y = start
    dq = deque([(x, y)])
    distance_map[y][x] = 1

    while dq:
        ex, ey = dq.popleft()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<m and 0<=ny<n and graph_map[ny][nx] == 1:
                    if distance_map[ny][nx] == 0:
                        dq.append((nx, ny))
                        distance_map[ny][nx] = distance_map[ey][ex] + 1
                    else:
                        distance_map[ny][nx] = min(distance_map[ny][nx], distance_map[ey][ex] + 1)

bfs((0,0))
print(distance_map[n-1][m-1])