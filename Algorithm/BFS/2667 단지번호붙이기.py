"""
아이디어 -> BFS
 - 2중 for -> 미방문 노드 중 값이 1인 것에 대해 BFS 실행
 - BFS 하면서 cnt += 1로 총 개수 세기 

BFS 자료구조
 - graph int[][]
 - 방문여부 bool[][]
 - 결과 list int[]
 """
import sys
from collections import deque
f = sys.stdin

n = int(f.readline())

graph_map = []
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    temp_list = list(str(f.readline().strip()))
    graph_map.append(list(map(int, temp_list)))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    dq = deque()
    dq.append((x,y))
    visited[y][x] = True

    cnt = 1

    while dq:
        ex, ey = dq.popleft()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<n and (graph_map[ny][nx] == 1):
                if (not visited[ny][nx]):
                    dq.append((nx, ny))
                    visited[ny][nx] = True
                    cnt += 1
    return cnt

result = []

for j in range(n):
    for i in range(n):
        if (graph_map[j][i] == 1) and (not visited[j][i]):
            result.append(bfs(j, i))

print(len(result))
print("\n".join(map(str, sorted(result))))