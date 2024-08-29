"""
아이디어
    - 최단 경로 찾기 -> bfs로 최소 깊이 찾을 수 있음 그리고 최소 깊이에 대해 가능한 모든 index 찾을 수 있음
    - 현재 상어 크기를 변수에 담고, 이웃 노드 중 어떤 물고기를 먹을 수 있는지 확인
    - 현재 상어 위치에서 bfs로 모두 돌았을 때, 먹을 수 있는 물고기가 없다면 break
"""

import sys
from collections import deque
f = sys.stdin
INF = sys.maxsize

n = int(f.readline())
grid = [list(map(int, f.readline().split())) for _ in range(n)]

# 현재 상어 위치 찾기 -> y, x
y, x = -1, -1
for j in range(n):
    if 9 in grid[j]:
        y = j
        x = grid[j].index(9)
        grid[y][x] = 0

shark = 2

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
def bfs(y,x):
    dq = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    fishes = []

    dq.append((0, y, x))
    visited[y][x] = True
    min_depth = INF

    while dq:
        depth, ey, ex = dq.popleft()
        if depth >= min_depth:
            break
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if (0<=ny<n) and (0<=nx<n) and visited[ny][nx] == False:
                if (0 < grid[ny][nx] < shark):
                    min_depth = depth + 1
                    fishes.append((ny, nx))

                    visited[ny][nx] = True
                    dq.append((depth + 1, ny, nx))
                elif (grid[ny][nx] in [0, shark]):
                    visited[ny][nx] = True
                    dq.append((depth + 1, ny, nx))

    return min_depth, fishes

time = 0    # 시간
cnt = 0     # 먹은 물고기 양

while True:
    min_depth, fishes = bfs(y, x)
    if min_depth == INF:
        print(time)
        break
    else:
        fishes.sort()
        ny, nx = fishes[0]

        time += min_depth   # 시간 업데이트
        y, x = ny, nx       # 상어 위치 업데이트
        grid[ny][nx] = 0    # 물고기 먹었다고 표시
        
        cnt += 1
        if cnt == shark:
            shark += 1
            cnt = 0