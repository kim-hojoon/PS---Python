"""
MST 문제
    추가 조건: 남초간 연결 & 여초간 연결은 사용할 수 없음

시간복잡도
    n: 10^3
    m: 10^4 => O(E logV)인 Prim 사용 가능

구현
1. 인접 리스트 만들기
    처음 input을 받을 때, 같은 남초 or 여초라면 인접 리스트에 추가하지 않음
2. MST 구현
    heap에 시작점 넣기
    heap이 빌 때까지,
        heap에서 pop하고, 해당 node가 미방문이라면
            방문 표시, 비용 추가, 연결 edge 모두 heap에 추가

"""

import sys
import heapq
f = sys.stdin

n, m = map(int, f.readline().split())
genders = [None] + list(map(str, f.readline().split())) # 성별 정보

# 인접 리스트 생성
edges = [ [] for _ in range(n+1) ] # 1번 node부터 n번 node까지
for _ in range(m):
    a, b, w = map(int, f.readline().split())
    if genders[a] != genders[b]:
        edges[a].append((w, b))
        edges[b].append((w, a))

heap = [(0, 1)] # 시작점 추가 (1번 node)
chk = [False for _ in range(n+1)]
ans = 0
cnt = 0 # 연결된 node 수

while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        ans += w
        cnt += 1
        for (near_w, near_node) in edges[next_node]:
            if chk[near_node] == False:
                heapq.heappush(heap, (near_w, near_node))

if cnt != n:
    print(-1)
else:
    print(ans)