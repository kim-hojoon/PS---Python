"""
MST 문제
    시간 복잡도
    m: 2x10^5
    n: 2x10^5 => O(n logn) 이하 => Prim 알고리즘 가능
"""
import sys
import heapq
f = sys.stdin

while True:
    m, n = map(int, f.readline().split()) # m: node 수, n: edge 수
    if m == 0 and n == 0: break

    edges = [[] for _ in range(m)] # 0번 node부터 m-1번 node까지
    weight_sum = 0
    for _ in range(n):
        a, b, w = map(int, f.readline().split())
        edges[a].append((w, b))
        edges[b].append((w, a))
        weight_sum += w
    
    heap = [(0, 0)] # 시작점 heap에 추가
    chk = [False for _ in range(m)]
    cost = 0 # MST의 비용 (최소 비용)
    while heap:
        w, next_node = heapq.heappop(heap)
        if chk[next_node] == False:
            chk[next_node] = True
            cost += w
            for near_w, near_node in edges[next_node]:
                if chk[near_node] == False:
                    heapq.heappush(heap, (near_w, near_node))
    print(weight_sum-cost)