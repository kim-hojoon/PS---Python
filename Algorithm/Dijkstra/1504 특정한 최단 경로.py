"""
목표: 1번 정점에서 N번으로 이동하는데, 두 경유지는 반드시 한 번 이상 찍어야함

아이디어: 다익스트라
    두 가지 가능성이 잇음
        1 -> a -> b -> N
        1 -> b -> a -> N
    
    # 1->a->b->N 먼저 계산해보자
    만약 [1-b] = [1-a] + [a-b] 라면 1-b에 a를 찍고 가는 게 존재한다는 것
        이때는 원하는 결과 = [1-b] + [b-n]
    만약 [1-b] < [1-a] + [a-b] 라면 1-b에 a를 찍고 가는 게 없는 것
        이때는 원하는 결과 = [1-a] + [a-b] + [b-n]

    # 1->b->a->N 계산해보기
    만약 [1-a] = [1-b] + [b-a] 라면 1-a에 b를 찍고 가는 게 존재한다는 것
        이때는 원하는 결과 = [1-a] + [a-n]
    만약 [1-a] < [1-b] + [b-a] 라면 1-b에 a를 찍고 가는 게 없는 것
        이때는 원하는 결과 = [1-b] + [b-a] + [a-n]

    이 아이디어에서는 총 [1-a] [1-b] [a-b] [a-n] [b-n] 총 5번의 다익스트라 사용
시간 복잡도 
    N: 8e2
    E: 2e5 => O(E lg N) => 가능!

"""
import sys
import heapq
f = sys.stdin
INF = sys.maxsize

n, e = map(int, f.readline().split())

# 인접 리스트 생성
edges = [[] for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int, f.readline().split())
    edges[u].append((w, v))
    edges[v].append((w, u))

a, b = map(int, f.readline().split())

def dijkstra(s, e):
    dist = [INF for _ in range(n+1)] # 1번부터 N번까지
    heap = [(0, s)] # 시작점 넣기
    dist[s] = 0

    while heap:
        ew, ev = heapq.heappop(heap)
        if ew != dist[ev]: continue
        for nw, nv in edges[ev]:
            if dist[nv] > ew + nw:
                dist[nv] = ew + nw
                heapq.heappush(heap, (dist[nv], nv))
    return dist[e]

one_a = dijkstra(1, a)
one_b = dijkstra(1, b)
a_b = dijkstra(a, b)
a_n = dijkstra(a, n)
b_n = dijkstra(b, n)

cand_1 = one_a + a_b + b_n
cand_2 = one_b + a_b + a_n

if min(cand_1,cand_2) >= INF: print(-1)
else: print(min(cand_1, cand_2))