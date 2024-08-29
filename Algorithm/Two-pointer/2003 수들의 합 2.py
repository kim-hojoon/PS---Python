"""
1. 아이디어
- 연속된 수의 합 -> two pointers

2. 변수
- res: 현재 수들의 합 
- cnt: 경우의 수
"""

import sys
f = sys.stdin

n, m = map(int, f.readline().split())
num_list = list(map(int, f.readline().split()))

right = 0
left = 0

res = 0
cnt = 0
while True:
    if res == m:
        cnt += 1
        if right == n:
            break
        res += num_list[right]
        right += 1
    elif res < m:
        if right == n:
            break
        res += num_list[right]
        right += 1
    else:
        res -= num_list[left]
        left += 1
print(cnt)