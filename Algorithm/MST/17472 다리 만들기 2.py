"""
MST 문제 -> Prim 알고리즘 사용

시간 복잡도
    N (세로): 10
    M (가로): 10

섬 정보 추가하기
    이중 for 문 -> 모든 좌표에 대해 BFS

인접리스트 만들기
    모든 점에서 BFS로 가로 세로로 다리를 뻗어보자.
    다음 좌표 값이
        1. 현재 섬 번호와 동일하다면 continue (섬의 끄트머리가 아니다 or 해당 방향이 아니다)
        2. 바다라면
            2-1. 이동거리를 1 추가하고, 해당 방향으로 한 칸 더 나아가본다.
            2-2. 다른 섬을 만날 때까지, 나아간다.
                2-2-1. 만약 섬을 만났을 때의 dist가 1이라면 break
                2-2-2. dist가 2 이상이라면 from 섬과 to 섬의 연결 비용을 구한 것이다! -> 인접 리스트에 추가한다.
"""
import sys
from collections import deque
import heapq
f = sys.stdin

n, m = map(int, f.readline().split())
grid = [ None for _ in range(n) ] # 그리드 형태로 지도를 구한다

for i in range(n):
    temp_list = list(map(int, f.readline().split()))
    grid[i] = temp_list

# BFS 이용해서 섬 정보 지도에 추가하기
visited = [ [False for _ in range(m)] for _ in range(n) ]
move = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(y, x, land_num):
    dq = deque()
    dq.append((y, x))

    while dq:
        ey, ex = dq.popleft()
        grid[ey][ex] = land_num # 섬 번호 붙이기
        for dy, dx in move:
            ny = ey + dy
            nx = ex + dx
            if 0<=nx<m and 0<=ny<n:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if grid[ny][nx] == 1:
                        dq.append((ny, nx))

land_num = 0 # 섬 번호 붙이기
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            if (grid[i][j] == 1): # 아직 방문 하지 않은 섬이라면
                land_num += 1
                bfs(i, j, land_num)

edges = [ set() for _ in range(land_num+1) ] # 1번부터 land_num까지
chk = [ [False for _ in range(m)] for _ in range(n) ]

# 인접 리스트 만들기
for y in range(n):
    for x in range(m):
        if not chk[y][x]:
            chk[y][x] = True
            if (grid[y][x] > 0): # 해당 좌표가 섬이라면
                from_land = grid[y][x] # 어느 섬에서 출발하는지 적기

                for dy, dx in move: # 다음 스텝으로 나가보기
                    ny = y + dy
                    nx = x + dx
                    dist = 0
                    while (0<=nx<m and 0<=ny<n): # 다음 스텝이 있을 때,
                        if (grid[ny][nx] == 0): # 다음이 바다라면 계속 진출!
                            ny += dy
                            nx += dx
                            dist += 1
                        elif (grid[ny][nx] == from_land): # 같은 바다라면 break
                            break
                        elif (dist < 2): # 거리가 2보다 작다면 break
                            break
                        else: # 다른 섬이면서 거리가 2이상이라면 인접 리스트에 추가
                            to_land = grid[ny][nx]
                            edges[from_land].add((dist, to_land))
                            edges[to_land].add((dist, from_land))
                            break
# MST 구현
heap = [(0, 1)] # 시작점 heap에 추가 (1번 node)
chk = [ False for _ in range(land_num+1) ]
cost = 0 # 총 비용
cnt = 0 # 섬 개수
while heap:
    w, next_node = heapq.heappop(heap)
    if not chk[next_node]:
        chk[next_node] = True
        cost += w
        cnt += 1
        for near_w, near_node in edges[next_node]:
            if not chk[near_node]:
                heapq.heappush(heap, (near_w, near_node))
if cnt != land_num:
    print(-1)
else:
    print(cost)