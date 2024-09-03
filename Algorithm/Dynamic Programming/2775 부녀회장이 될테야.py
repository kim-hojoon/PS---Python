"""
아이디어: 합을 구한다? -> 점화식 -> DP

조건: 1 <= k, n <= 14

모든 경우의 수 구해놓자 => 총 14*14 번
"""

import sys
f = sys.stdin

t = int(f.readline())
test_list = [ [ int(f.readline()) for _ in range(2) ] for _ in range(t) ]

APT = [ [i for i in range(0,15)] ] # 0층 사람들 정보

for f_num in range(1, 15):
    current_floor = [0]
    under_floor = APT[f_num-1]
    for room in range(1, 15):
        under_num = under_floor[room]
        left_num = current_floor[room-1]
        current_floor.append(under_num + left_num)
    APT.append(current_floor)

for k, n in test_list:
    print(APT[k][n])