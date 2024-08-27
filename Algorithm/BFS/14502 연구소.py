"""
아이디어
- 바이러스 확산 -> BFS로 계산 가능
- 벽을 반드시 3개 세워야 함 -> 벽을 세울 수 있는 모든 경우의 수에 대해 BFS로 영역 계산? for 문
- 3 <= N, M <= 8 이므로 최대 맵 크기 64에 대해 경우의 수는 64C3이므로 크지 않음
"""

import sys
from collections import deque
from itertools import combinations
f = sys.stdin


n, m = map(int, f.readline().split())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

string_list = []
for _ in range(n):
    string_list.append(str(f.readline().strip()))
map_string = "/".join(string_list)


def bfs(y, x, map):
    dq = deque()
    dq.append((y, x))

    while dq:
        ey, ex = dq.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if (0<=nx<m) and (0<=ny<n) and (map[ny][nx] == "0"):
                map[ny][nx] = "2"
                dq.append((ny, nx))

def cal_area(map):
    for j in range(n):
        for i in range(m):
            if map[j][i] == "2":
                bfs(j, i, map)
    area = 0
    for row in map:
        area += row.count("0")
    return area

index = 0
zero_index_list = []

while True:
    try:
        next_i = map_string.index("0", index+1)
        zero_index_list.append(next_i)
        index = next_i
    except:
        break

max_area = 0
for i in range(len(zero_index_list) - 2):
    for j in range(i+1, len(zero_index_list) - 1):
        for k in range(j+1, len(zero_index_list)):
            new_map_list = list(map_string)
            new_map_list[zero_index_list[i]] = "1"
            new_map_list[zero_index_list[j]] = "1"
            new_map_list[zero_index_list[k]] = "1"
            new_map_string = " ".join(new_map_list)
            temp_list = new_map_string.split("/")
            new_map = [row.split() for row in temp_list]
            max_area = max(max_area, cal_area(new_map))
print(max_area)