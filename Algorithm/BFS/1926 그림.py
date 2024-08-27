"""
1. 아이디어
- 2중 for -> 값 1 && 방문 X -> BFS
- BFS마다 그림개수 += 1 , 최대값 갱신

2. 시간복잡도
O(V+E)
V : m * n
E : 4 * m * n
V + E : 5 * 500 * 500 = 125 * 10^4 = 1.25 * 10^6 < 2 * 10^8 (2억)

# 자료구조
- 그래프 -> int[][]
- 방문여부 -> bool[][]
- BFS -> Queue
"""

import sys
from collections import deque

f = sys.stdin

n, m = map(int, f.readline().split())
paint_map = [list(map(int, f.readline().split())) for _ in range(n)]

chk = [[False for _ in range(m)] for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    dq = deque()
    dq.append((x,y))
    size = 1
    while dq:
        ex, ey = dq.popleft()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if paint_map[ny][nx] == 1 and chk[ny][nx] == False:
                    size += 1
                    chk[ny][nx] = True
                    dq.append((nx, ny))
    return(size)

cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if paint_map[j][i] == 1 and chk[j][i] == False:
            # 그림 개수 & 방문 여부 update
            chk[j][i] = True
            cnt += 1
            # 최대값 update
            maxv = max(maxv, bfs(j,i))

print(f"{cnt}\n{maxv}")