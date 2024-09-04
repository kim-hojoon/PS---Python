"""
아이디어
    n에서부터 3가지로 계속 뻗어나가기
    bfs로 k를 찾을 때까지 풀기!!

시간복잡도
    n: 1e5
    k: 1e5
    전체 좌표 크기: 1e5 -> n logn도 가능!

구현
    자료구조
    1. 시간 리스트 time: 해당 지점에 도달하기까지 걸리는 최소 시간 (x축 좌표)
    2. 데크 dq: bfs를 위함
    
    구현
    처음 time 모든 점 INF로 초기화 (미방문 표시)
    시작점 n dq에 넣기 & 시작점 time 0으로 초기화

    dq가 빌 때까지 while
        x 꺼내기 (popleft)
        만약 x가 k와 같다면 dq[x] return

        x의 이웃 +1, -1, * 2에 대해
            1. 범위를 벗어나면 break
            2. 이미 방문했다면 (time이 INF가 아니라면) break
            
            if *2 라면
                time[nx] = time[x]로 update
                dq appendleft
            else:
                time[nx] = time[x]
                dq append()
"""
import sys
from collections import deque
f = sys.stdin
INF = sys.maxsize

n, k = map(int, f.readline().split())

axis_size = 100001

time = [ INF for _ in range(axis_size) ] # axis 사이즈 만큼 time 리스트 초기화
dq = deque()

time[n] = 0
dq.append(n)

while dq:
    x = dq.popleft()
    if x == k:
        print(f"{time[x]}")
        break
    
    for nx in (x-1, x+1, x*2):
        if (0 <= nx < axis_size) and time[nx] == INF:
            if nx == 2*x:
                time[nx] = time[x]
                dq.appendleft(nx)
            else:
                time[nx] = time[x] + 1
                dq.append(nx)
