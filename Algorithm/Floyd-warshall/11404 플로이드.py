"""
모든 정점에서 모든 정점으로의 최단 거리 -> 플로이드 워셜 문제

변수
- 거리 배열 : int[][]

구현
- 거리 배열 INF로 초기화
- 본인 to 본인 0으로 초기화
- input으로 받은 비용 넣기 (최솟값으로 넣기)
"""
import sys
f = sys.stdin
INF = sys.maxsize

n = int(f.readline())
m = int(f.readline())

dist = [ [INF for _ in range(n+1)] for _ in range(n+1) ] # INF로 초기화
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, w = map(int, f.readline().split())
    dist[a][b] = min(dist[a][b], w)

# 플로이드 워셜 구현
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF: print("0", end=" ")
        else: print(dist[i][j], end=" ")
    print()
