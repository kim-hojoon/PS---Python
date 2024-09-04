"""
모든 학생들 간 비교 -> 플로이드 워셜로 풀기

시간 복잡도
O(V^3) => (5e^2)^3 = 125 e^6 => e^8으로 아슬아슬하게 가능!?

아이디어
    만약 4번 node에 대해 다른 모든 node와의 크기 비교가 가능한 경우, 해당 학생의 키 순서를 알 수 있다
    따라서 본인보다 크다면 1, 작다면 -1를 거리 배열에 넣고
    모두 업데이트했을 때 본인 row에 비교가 불가능한 게 있다면 학생은 순서 알 수 없음 (즉 INF가 있으면 알 수 없음)

변수
    거리 배열: 본인 0, 알 수 없음 INF, 본인이 더 큼 1, 본인이 더 작음 -1

구현
    - 거리 배열 모두 INF로 설정
    - 거리 배열 본인 to 본인은 0으로 설정
    - input으로 받은 정보 입력 dist[a][b] = -1 그리고 dist[b][a] = 1

    - 삼중 for문을 돌면서
        - 경유지를 찍었을 때 모두 -1이면 -1 넣기 / 모두 1이면 1 넣기

    - 거리 배열의 모든 row를 돌면서 INF가 없으면 ans += 1
"""
import sys
f = sys.stdin
INF = sys.maxsize

n, m = map(int, f.readline().split())

dist = [ [INF] * (n+1) for _ in range(n+1) ] # INF로 초기화
for i in range(1, n+1) : dist[i][i] = 0 # 0으로 초기화

for _ in range(m):
    a, b = map(int, f.readline().split())
    dist[a][b] = -1 # a는 b보다 작다
    dist[b][a] = 1 # b는 a보다 크다

# 플로이드 워셜 구현
for k in range(1, n+1): # 경
    for i in range(1, n+1): # 시
        for j in range(1, n+1): # 끝
            if dist[i][k] == dist[k][j] != INF:
                dist[i][j] = dist[i][k]

ans = 0
for i in range(1, n+1):
    row = dist[i][1:]
    if INF not in row:
        ans += 1
print(ans)