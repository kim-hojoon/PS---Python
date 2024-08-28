import sys
sys.setrecursionlimit(1000000)
f = sys.stdin


dy, dx = [1,-1, 0, 0, 1, -1, 1, -1], [0, 0, 1, -1, 1, -1, -1, 1]
def dfs(y, x, w, h, visited):
    visited[y][x] = True
    for k in range(8):
        ny = y + dy[k]
        nx = x + dx[k]
        if (0<=nx<w) and (0<=ny<h) and grid[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx, w, h, visited)

while True:
    w, h = map(int, f.readline().split())
    if w == 0 and h == 0:
        break

    grid = [ list(map(int, f.readline().split())) for _ in range(h) ]
    visited = [[False for _ in range(w)] for _ in range(h)]
    
    cnt = 0
    for j in range(h):
        for i in range(w):
            if grid[j][i] == 1 and not visited[j][i]:
                cnt += 1
                dfs(j, i, w, h, visited)
    print(cnt)