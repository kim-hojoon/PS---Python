import sys
from collections import deque
f = sys.stdin

n = int(f.readline())

grid = [ list(map(str, f.readline().rstrip())) for _ in range(n)]
visited_1 = [ [False for _ in range(n)] for _ in range(n)]
visited_2 = [ [False for _ in range(n)] for _ in range(n)]

dy, dx = [1,-1,0,0], [0,0,1,-1]

def bfs(y, x, grid, visited, dq):
    dq.append((y, x))
    visited[y][x] = True
    color = grid[y][x]

    while dq:
        ey, ex = dq.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=nx<n and 0<=ny<n:
                if (not visited[ny][nx]) and grid[ny][nx] == color:
                    dq.append((ny, nx))
                    visited[ny][nx] = True

new_grid = [ ["R" if grid[y][x] == "G" else grid[y][x] for x in range(n)] for y in range(n)]

cnt_1 = 0
cnt_2 = 0

dq_1 = deque()
dq_2 = deque()

for j in range(n):
    for i in range(n):
        new_grid[j][i]
        if not visited_1[j][i]:
            cnt_1 += 1
            bfs(j,i, grid, visited_1, dq_1)
        if not visited_2[j][i]:
            cnt_2 += 1
            bfs(j,i, new_grid, visited_2, dq_2)

print(f"{cnt_1} {cnt_2}")