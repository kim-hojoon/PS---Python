"""
한 점에서 모든 점으로의 최단 거리 -> 다익스트라

시간복잡도
    V : 2e4
    E : 3e5
    다익스트라 O(E lgV) => 대충 6e6으로 가능!

아이디어 다익스트라 구현
    자료 구조
    1. 연결 리스트 edge
    2. 거리 리스트 dist (지금까지의 각 점까지 가는 데 필요한 최소 비용)
    3. 최소 힙 heap

    구현 순서
        모든 dist 값 INF로 설정
        시작점 dist = 0 & heap에 시작점 추가
        heap이 빌 때까지,
            ew, ev 꺼냄
                만약 ew가 dist의 값보다 크면 (outdated 의미) continue
            ev의 모든 이웃에 대해,
                dist의 값보다 간선 통과 값이 적다면, 갱신!
                and heap에 추가
"""
import sys
import heapq
f = sys.stdin
INF = sys.maxsize

v, e = map(int, f.readline().split())
k = int(f.readline())

edges = [[] for _ in range(v+1)] # 1번 node부터 v번 node까지
for _ in range(e):
    a, b, w = map(int, f.readline().split())
    edges[a].append((w, b))

dist = [INF for _ in range(v+1)] # 1번 node부터 v번 node까지
heap = [(0, k)] # 시작점 추가
dist[k] = 0

while heap:
    ew, ev = heapq.heappop(heap)
    if ew != dist[ev]: continue # outdated라면

    for nw, nv in edges[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, (dist[nv], nv))

for i in range(1, v+1):
    if dist[i] == INF : print("INF")
    else: print(dist[i])