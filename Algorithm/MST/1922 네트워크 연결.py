"""
MST 문제 -> Prim 알고리즘
    - 컴퓨터: node
    - 전선: edge
    - 비용: weight
"""
import sys
import heapq
f = sys.stdin

n = int(f.readline()) # node 수
m = int(f.readline()) # edge 수

edges = [[] for _ in range(n+1)] # 인접 리스트 만들기

for _ in range(m):
    a, b, w = map(int, f.readline().split())
    edges[a].append((w, b))
    edges[b].append((w, a))

heap = [(0, 1)] # heap에 시작점 추가
chk = [ False for _ in range(n+1) ]
ans = 0
while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True   # 방문 표시
        ans += w                # 비용 추가
        for weight, node in edges[next_node]:
            heapq.heappush(heap, (weight, node))    # 인접 edge 모두 추가
print(ans)
