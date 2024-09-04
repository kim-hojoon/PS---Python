"""
모든 점에서 한 점으로 오는 데 걸리는 최소 시간
한 점에서 모든 점으로 가는데 걸리는 최소 시간

다익스트라 문제!

사실 전후 관계만 다를 뿐, 한점 <-> 모든점이라는 것은 동일하다
따라서 한 점에서 모든 점으로 가는 데 걸리는 최소 시간은 단방향 그래프에서 다익스트라를 사용하면 바로 구할 수 있음
+ 모든 점에서 한 점으로 가는 데 걸리는 최소 시간은 단방향 그래프의 방향을 뒤집어서 다익스트라를 사용하면 됨

시간복잡도 O(m logn) 2번 => 2e5 가능

자료구조
1. 인접 리스트 (정방향) edges
2. 인접 리스트 (역방향) rev_edges
3. 거리 리스트 dist
4. 최소 힙 heap

구현 다익스트라 그대로 구현
    1. 모든 dist INF로 초기화
    2. 시작점 heap에 넣고 dist 0으로 설정
    3. heap이 빌 때까지,
        heap에서 ew, ev 꺼내고
            해당 ew != dist[ev] 라면 continue
        ev의 모든 이웃 nv에 대해,
            dist[nv] > ew + nw 라면
            dist 갱신 heap update
"""
import sys
import heapq
f = sys.stdin
INF = sys.maxsize

n, m, x = map(int, f.readline().split())

edges = [[] for _ in range(n+1)] # 1번부터 n번까지 (정방향)
edges_rev = [[] for _ in range(n+1)] # 1번부터 n번까지 (역방향)

# 인접리스트 생성
for _ in range(m):
    a, b, w = map(int, f.readline().split())
    edges[a].append((w, b))
    edges_rev[b].append((w, a))

# 정방향 다익스트라 구현
dist = [INF for _ in range(n+1)]
heap = [(0, x)]
dist[x] = 0
while heap:
    ew, ev = heapq.heappop(heap)
    if ew != dist[ev]: continue

    for nw, nv in edges[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, (dist[nv], nv))

# 역방향 다익스트라 구현
dist_rev = [INF for _ in range(n+1)]
heap = [(0, x)]
dist_rev[x] = 0
while heap:
    ew, ev = heapq.heappop(heap)
    if ew != dist_rev[ev]: continue

    for nw, nv in edges_rev[ev]:
        if dist_rev[nv] > ew + nw:
            dist_rev[nv] = ew + nw
            heapq.heappush(heap, (dist_rev[nv], nv))

maxv = 0
for i in range(1, n+1):
    temp = dist[i] + dist_rev[i]
    maxv = max(maxv, temp)
print(maxv)