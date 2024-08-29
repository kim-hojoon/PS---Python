import sys
from collections import deque
f = sys.stdin

n = int(f.readline())
k = int(f.readline())
apple_list = [list(map(int, f.readline().split())) for _ in range(k)]
l  = int(f.readline())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

drift_list = deque()
for _ in range(l):
    drift_time, drift_d = f.readline().split()
    drift_time = int(drift_time)
    if drift_d == "L": drift_d = -1
    elif drift_d == "D": drift_d = 1
    drift_list.append((drift_time, drift_d))

grid = [[0 for _ in range(n+1)] for _ in range(n+1)] # 0: 빈칸, 1: 몸, 2: 사과 / index 0은 사용하지 않음
for y, x in apple_list:
    grid[y][x] = 2


snake = deque()
snake.appendleft((1, 1))

time = 0
current_d = 1
drift_time, drift_d = drift_list.popleft()

grid[1][1] = 1
while True:
    time += 1
    y, x = snake[0] # 머리 가져오기

    ny = y + dy[current_d]
    nx = x + dx[current_d]

    if (1<=nx<=n) and (1<=ny<=n):
        if grid[ny][nx] == 1:       # 다음 칸이 몸이면 break
            break
        elif grid[ny][nx] == 2:     # 다음 칸이 사과면 head만 늘리기
            snake.appendleft((ny, nx))
            grid[ny][nx] = 1
        else:                       # 다음 칸이 빈칸이면 head 늘리고 tail 줄이기
            snake.appendleft((ny, nx))
            grid[ny][nx] = 1
            ty, tx = snake.pop()
            grid[ty][tx] = 0
    else:                           # 다음 칸이 벽이면 break
        break

    if time == drift_time:          # drift_t초가 지나면 drift
        current_d = (current_d + drift_d) % 4
        if drift_list:              # drift_list가 안 비었으면 update
            drift_time, drift_d = drift_list.popleft()
        else:                       # drift_list가 비었으면 -1로 update
            drift_time = -1

print(time)