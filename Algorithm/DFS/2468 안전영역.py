"""
아이디어
- 1중 for 문으로 장마 높이 설정 1이상 100이하
- 각 장마 높이마다 총 안전영역의 개수 구함 -> DFS
- DFS 구현 -> 2중 for문 -> not visited 중 장마에 잠기지 않은 영역에서 DFS 시작 cnt += 1
"""

import sys
sys.setrecursionlimit(1000000)
f = sys.stdin

n = int(f.readline())

grid = [ list(map(int, f.readline().split())) for _ in range(n) ]

dy, dx = [1,-1,0,0], [0,0,1,-1]
def dfs(y, x, threshold):
    visited[y][x] = True
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if (0<=nx<n) and (0<=ny<n) and (not visited[ny][nx]) and (grid[ny][nx] > threshold):
            dfs(ny, nx, threshold)

max_cnt = 0

for threshold in range(101):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for j in range(n):
        for i in range(n):
            if (grid[j][i] > threshold) and not visited[j][i]:
                cnt += 1
                dfs(j,i, threshold)
    if cnt == 0:
        break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)