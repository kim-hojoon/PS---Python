"""
# 주의
grid에서 북쪽은 dy = -1, dx = 0이다!!! 위로 올라가는 것은 y값이 줄어드는 것. 바보야!
"""

import sys
f = sys.stdin

n, m = map(int, f.readline().split())
y, x, d = map(int, f.readline().split())
grid  = [ list(map(int, f.readline().split())) for _ in range(n) ]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = 0

while True:
    if grid[y][x] == 0:
        ans += 1
        grid[y][x] = 2
    
    sw = True
    for i in range(1, 5):
        ny = y + dy[(d-i)%4]
        nx = x + dx[(d-i)%4]
        if (0<=nx<m and 0<=ny<n):
            if grid[ny][nx] == 0:
                d = (d-i)%4
                y, x = ny, nx
                sw = False
                break
    if sw:
        ny = y - dy[d]
        nx = x - dx[d]
        if (0<=nx<m and 0<=ny<n):
            if grid[ny][nx] == 1:
                break
            else:
                y, x = ny, nx
        else:
            break
print(ans)