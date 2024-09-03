"""
시간복잡도
    n <= 10

아이디어
    1 = 1 (1가지)
    2 = 2 & 1 + 1 (2가지)
    3 = 3 & 2 + 1 & 1 + 1 + 1 & 1 + 2 (4가지)
    4 = [3의 경우의 수] & [2의 경우의 수] & [1의 경우의 수]
    5 = [4의 경우의 수] & [3의 경우의 수] & [2의 경우의 수]
"""

import sys
f = sys.stdin

t = int(f.readline())
test_list = [ int(f.readline()) for _ in range(t) ]

pb_list = [0, 1, 2, 4]

for num in range(4, 11):
    pb_list.append(pb_list[num-1] + pb_list[num-2] + pb_list[num-3])

for test in test_list:
    print(pb_list[test])