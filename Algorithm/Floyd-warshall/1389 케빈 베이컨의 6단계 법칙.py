"""
모든 사람 <-> 모든 사람 최단 거리 => 플로이드 워셜 문제!
조건: 양방향 그래프
변수
    - 거리 리스트: int[][]
구현
    - 거리 리스트 모두 INF로 초기화
    - 거리 리스트 본인 to 본인을 0으로 초기화
    - input으로 받는 친구 관계 정보를 거리 리스트에 넣기
        dist[a][b] = 1 그리고 dist[b][a] = 1
    
    - dist의 각 row의 합이 가장 작은 번호를 print (겹치면 번호 작은 사람)
"""
import sys
f = sys.stdin
INF = sys.maxsize

n, m = map(int, f.readline().split())
dist = [[INF for _ in range(n+1)] for _ in range(n+1)] # 1번부터 n번까지 INF로 초기화
for i in range(1, n+1): dist[i][i] = 0

for _ in range(m):
    a, b = map(int, f.readline().split())
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드 워셜 구현
for k in range(1, n+1): # 경
    for i in range(1, n+1): # 시
        for j in range(1, n+1): # 끝
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

min_score = INF
ans = 0
for i in range(1, n+1):
    row = dist[i][1:] # 0번 index 정보 자르기
    kb_score = sum(row)
    if min_score > kb_score:
        min_score = kb_score
        ans = i
print(ans)