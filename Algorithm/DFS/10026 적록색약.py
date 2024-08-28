import sys
sys.setrecursionlimit(1000000) # DFS 활용 시, recursion limit을 늘려주는 게 좋다
f = sys.stdin

n = int(f.readline())

grid = [ list(map(str, f.readline().rstrip())) for _ in range(n)]
visited_1 = [ [False for _ in range(n)] for _ in range(n)]
visited_2 = [ [False for _ in range(n)] for _ in range(n)]

dy, dx = [1,-1,0,0], [0,0,1,-1]
def dfs(y, x, grid, visited):
    visited[y][x] = True
    color = grid[y][x]

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=nx<n and 0<=ny<n:
            if not visited[ny][nx] and grid[ny][nx] == color:
                dfs(ny, nx, grid, visited)

new_grid = [ ["R" if grid[y][x] == "G" else grid[y][x] for x in range(n)] for y in range(n)]

cnt_1 = 0
cnt_2 = 0
for j in range(n):
    for i in range(n):
        new_grid[j][i]
        if not visited_1[j][i]:
            cnt_1 += 1
            dfs(j,i, grid, visited_1)
        if not visited_2[j][i]:
            cnt_2 += 1
            dfs(j,i, new_grid, visited_2)

print(f"{cnt_1} {cnt_2}")