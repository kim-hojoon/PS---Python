"""
MST 문제 -> Prim으로 해결

시간복잡도
    n (node 수): 1000
        => edge 수는 n^2: 10^6 => O(e loge) 알고리즘 가능 (Prim 가능)

인접 리스트 얻기
    모든 경우의 수에 대해 비용이 주어지기에 n^2 크기의 int[][] 리스트에 담기
"""
import sys
import heapq
f = sys.stdin

n = int(f.readline())

# 인접 리스트 구하기
edges = [[] for _ in range(n)]
for i in range(n): # 0번 node부터 n-1번 node까지
    cost_list = list(map(int, f.readline().split()))
    for j, cost in enumerate(cost_list):
        if i != j:
            edges[i].append((cost, j))
            edges[j].append((cost, i))

# MST 구현
heap = [(0, 0)] # 시작점 heap에 추가 (0번 node)
chk = [False for _ in range(n)]
ans = 0 # 비용
while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        ans += w
        for near_w, near_node in edges[next_node]:
            if chk[near_node] == False:
                heapq.heappush(heap, (near_w, near_node))
print(ans)
