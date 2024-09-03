"""
MST 문제 - Prim

시간복잡도
n: 100

인접리스트 만들기
모든 좌표 간 거리 리스트에 넣기 -> n^2

"""
import sys
import heapq
import math
f = sys.stdin

n = int(f.readline())

cords = [ (0.0, 0.0) ] + [ list(map(float, f.readline().split())) for _ in range(n) ]

edges = [ [] for _ in range(n+1) ]
for i in range(1,n+1):
    for j in range(i+1, n+1):
        w = math.dist(cords[i], cords[j])
        edges[i].append((w, j))
        edges[j].append((w, i))

heap = [(0, 1)]
chk = [False for _ in range(n+1)]
ans = 0

while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True   # 방문 여부 체크
        ans += w                # 비용 추가
        for near_w, near_node in edges[next_node]:
            if chk[near_node] == False:
                heapq.heappush(heap, (near_w, near_node))

print(ans)