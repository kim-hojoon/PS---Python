"""
아이디어
    인구 이동이 끝날 때 까지 while True:
        이중 for 문 -> BFS로 돌면서 모든 국경을 연다
        -> 연합 하나가 구해지면, 해당 연합끼리 인구 이동 (평균 대입)
        BFS로 구한 총 연합의 개수가 n**2라면 break
"""

import sys
from collections import deque
f = sys.stdin

n, l, r = map(int, f.readline().split())
grid = [ list(map(int, f.readline().split())) for _ in range(n) ]

# 0: 북, 1: 동, 2: 남, 3: 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    dq = deque()
    union_list = []

    dq.append((y,x))
    visited[y][x] = True
    union_list.append((y,x))
    people = grid[y][x]

    while dq:
        ey, ex = dq.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if (0<=nx<n) and (0<=ny<n) and not visited[ny][nx]:
                if l <= abs(grid[ey][ex] - grid[ny][nx]) <= r:
                    dq.append((ny, nx))
                    visited[ny][nx] = True
                    union_list.append((ny, nx))
                    people += grid[ny][nx]
    return union_list, people // len(union_list)

day = 0
while True:
    visited = [ [False for _ in range(n)] for _ in range(n) ]
    union_num = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                union_num += 1
                union_list, num = bfs(y, x)
                # 연합간 인구 이동 (평균 대입)
                for uy, ux in union_list:
                    grid[uy][ux] = num
    if union_num == n**2:
        print(day)
        break
    day += 1