"""
한 점에서 다른 한 점으로 이동하는 최단 거리 -> 다익스트라

아이디어
    다익스트라로 시작점에서 모든 점까지의 최단 거리를 구하고
    도착점까지의 비용을 print한다

시간복잡도
    N: 1e3
    M: 1e5
    => 다익스트라 알고리즘 시간복잡도 O(E lgV) => 대충 2e4 정도로 충분함

다익스트라 구현
    자료구조
    1. 인접 리스트 edges
    2. 거리 리스트 dist
    3. 최소 힙 heap

    구현
        dist INF로 초기화
        시작점 heap에 넣기 & 시작점 dist 0으로 설정

        heap이 빌 때까지,
            ew, ev 꺼내기
                ew가 dist[ev]와 다르면 continue (outdated)
            ev의 모든 연결 노드에 대해
                dist[nv] > ew + w라면
                    dist 갱싱 & heap에 추가
"""
import sys
import heapq
f = sys.stdin
INF = sys.maxsize

n = int(f.readline()) # 노드 수
m = int(f.readline()) # 엣지 수

# 인접 리스트 생성
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, f.readline().split())
    edges[a].append((w, b))

start, end = map(int, f.readline().split())

# 다익스트라 구현
dist = [INF for _ in range(n+1)]
heap = [(0, start)]
dist[start] = 0

while heap:
    ew, ev = heapq.heappop(heap) # each 정보
    if ew != dist[ev]: continue # outdated된 ew라면 continue

    for nw, nv in edges[ev]: # near 정보
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, (dist[nv], nv))

print(dist[end])