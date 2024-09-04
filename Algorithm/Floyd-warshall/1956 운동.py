"""
모든 점에서 모든 점으로의 최단 거리 -> 플로이드 워셜 문제

아이디어:
    플로이드 워셜에서 본인 to 본인을 0으로 초기화 하지 않으면? => 사이클 최소 비용을 구할 수 있음

시간복잡도:
O(V^3) => 4e2^3 => 64e6 < 1e8 가능!

변수
    - 거리 배열 : dist[][] => INF는 경로 찾기 불가능 
구현
    - 거리 배열 INF로 초기화
    - input으로 받은 것 거리 배열에 반영 (단방향 그래프 주의)
    - 삼중 for 문으로 최단 거리 업데이트

    - for 문으로 대각선 요소 돌면서 최소값 찾기
"""
import sys
f = sys.stdin
INF = sys.maxsize

v, e = map(int, f.readline().split())

dist = [ [INF for _ in range(v+1)] for _ in range(v+1) ] # 1번부터 v번까지 & INF로 초기화

for _ in range(e):
    a, b, w = map(int, f.readline().split())
    dist[a][b] = w

# 플로이드 워셜 구현
for k in range(1, v+1): # 경
    for i in range(1, v+1): # 시
        for j in range(1, v+1): # 끝
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = INF
for i in range(1, v+1):
    ans = min(ans, dist[i][i])

if ans == INF: print(-1)
else: print(ans)