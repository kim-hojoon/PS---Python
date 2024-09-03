"""
아이디어: 그리디 -> 기다리는 사람 중 가장 시간이 적게 걸리는 사람이 먼저 뽑는 게 무조건 유리하다
"""

import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))

num_list.sort()

ans = 0
count = n
for num in num_list:
    ans += num * count
    count -= 1
print(ans)