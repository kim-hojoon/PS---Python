"""
MST 문제 -> Prim 알고리즘

시간복잡도
    - n = 10^5 => O(n logn) 가능

인접리스트 만드는 비용
    - 모든 경우의 수 따지기 -> n^2 => 불가능
    - 모든 경우의 수에 대해 미리 인접 리스트를 만드는 것은 불가능.
    -> 따라서 Prim 알고리즘 중, near_edge 추가할 때, 비용을 계산하자!
"""
import copy
import sys
import heapq
f = sys.stdin
INF = sys.maxsize

n = int(f.readline())

cords = [ list(map(int, f.readline().split())) + [i] for i in range(n) ] # 0번 행성부터 (n-1)번 행성까지

cords_x = copy.deepcopy(cords)
cords_y = copy.deepcopy(cords)
cords_z = copy.deepcopy(cords)
cords_x.sort(key=lambda v: v[0])
cords_y.sort(key=lambda v: v[1])
cords_z.sort(key=lambda v: v[2])

edges = [[] for _ in range(n)]
for i in range(1, n):
    a, b, c, i1 = cords_x[i-1]
    x, y, z, i2 = cords_x[i]
    cost = min(abs(a-x), abs(b-y), abs(c-z))
    edges[i1].append((cost, i2))
    edges[i2].append((cost, i1))

    a, b, c, i1 = cords_y[i-1]
    x, y, z, i2 = cords_y[i]
    cost = min(abs(a-x), abs(b-y), abs(c-z))
    edges[i1].append((cost, i2))
    edges[i2].append((cost, i1))

    a, b, c, i1 = cords_z[i-1]
    x, y, z, i2 = cords_z[i]
    cost = min(abs(a-x), abs(b-y), abs(c-z))
    edges[i1].append((cost, i2))
    edges[i2].append((cost, i1))

heap = [(0, 0)]
chk = [False for _ in range(n)]
ans = 0
while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        ans += w
        for (near_w, near_node) in edges[next_node]:
            heapq.heappush(heap, (near_w, near_node))
print(ans)