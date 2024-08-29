"""
연속적인 수의 합의 최대 -> Two pointer 문제
"""

import sys
f = sys.stdin

n, k = map(int, f.readline().split())
num_list = list(map(int, f.readline().split()))

left = 0    # 앞으로 뺄 곳의 index
right = k   # 앞으로 더할 곳의 index

each = sum(num_list[0:k])

maxv = each

while right < n: # right의 최대값 = n-1
    each -= num_list[left]
    each += num_list[right]
    left += 1
    right += 1

    maxv = max(maxv, each)

print(maxv)