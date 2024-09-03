"""
MST 문제

구현 순서
- heap에 시작점 넣기
- heap이 빌 때까지 다음 작업 반복
    heappop으로 최소값 꺼내기
    - 만약 next_node 미방문이라면
        - 비용 추가, 방문 표시, 연결 edge 모두 heap에 넣기
"""

import sys
import heapq
f = sys.stdin

v, e = map(int, f.readline().split())

edges = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, f.readline().split())
    edges[a].append((w, b))
    edges[b].append((w, a))

chk = [False for _ in range(v+1)]
heap = [(0, 1)]
ans = 0
while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        ans += w
        for weight, edge in edges[next_node]:
            heapq.heappush(heap, (weight, edge))
print(ans)