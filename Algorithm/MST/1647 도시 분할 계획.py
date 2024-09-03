"""
아이디어
MST 문제 하지만 MST가 2개여야함 -> 전체 MST를 구하고 해당 edge 중 가장 비용이 높은 것을 제거하면 됨!

시간복잡도
n: 10^5
m: 10^6
Prim의 시간복잡도 -> O(m logm): 2*10^8 -> 10^8보다 큼!!!!!


"""
import sys
import heapq
f = sys.stdin

n, m = map(int, f.readline().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, f.readline().split())
    edges[a].append((w, b))
    edges[b].append((w, a))

heap = [(0, 1)]
chk = [ False for _ in range(n+1) ]
ans = 0
max_w = 0

while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        ans += w
        max_w = max(max_w, w)
        for near_w, near_node in edges[next_node]:
            if chk[near_node] == False:
                heapq.heappush(heap, (near_w, near_node))

print(ans - max_w)