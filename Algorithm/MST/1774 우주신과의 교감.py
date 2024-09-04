"""
MST 문제
    비용 - 2차원 좌표의 유클리드 거리
    추가 조건 - 이미 연결되어 있는 통로가 있을 수 있음 (해당 node 간 비용을 0으로 생각하면 됨)

시간복잡도
    n (node 수): 1000
    m (이미 연결된 edge 수): 1000

    따라서 모든 node의 조합에 대한 비용을 계산해서 인접리스트를 만들어도 n^2 이라 가능함!!

구현
    1. n의 좌표를 이용해 모든 조합에 대해 비용 리스트를 계산함
    2. 이미 연결된 통로가 이미 있다면 인접리스트의 비용을 0으로 update함
"""

import sys
import heapq
f = sys.stdin

n, m = map(int, f.readline().split()) # n: node 수, m: 이미 연결된 edge 수

cords = [ (0, 0) for _ in range(n+1) ] # 좌표 리스트
edges = [[] for _ in range(n+1)] # 인접 리스트
zero_connected = set() # 이미 연결된 통로 정보

for i in range(1, n+1): # 1번 node부터 n번 node 까지
    x, y = map(int, f.readline().split())
    cords[i] = (x, y)

for _ in range(1, m+1):
    a, b = map(int, f.readline().split())
    edges[a].append((0, b))
    edges[b].append((0, a))
    zero_connected.add((min(a, b), max(a, b)))

def cal_dist(i, j):
    x1, y1 = cords[i]
    x2, y2 = cords[j]
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return dist

# 인접 리스트 완성
for i in range(1, n):
    for j in range(i+1, n+1):
        if (i, j) not in zero_connected:
            w = cal_dist(i, j)
            edges[i].append((w, j))
            edges[j].append((w, i))

# MST 구현
heap = [(0, 1)] # 시작점 추가 (1번 노드)
chk = [ False for _ in range(n+1) ]
ans = 0

while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        ans += w
        for near_w, near_node in edges[next_node]:
            if chk[near_node] == False:
                heapq.heappush(heap, (near_w, near_node))

print(f"{ans:.2f}")