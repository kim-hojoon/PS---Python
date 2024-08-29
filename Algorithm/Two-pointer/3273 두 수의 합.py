"""
두 수의 합 -> 모든 수의 조합 O(n**2) -> 10**10 -> 안 됨
정렬 후 two pointer -> O(n logn) -> 10**5 x 10^2 -> 10**7
"""

import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))
x = int(f.readline())

num_list.sort()

left = 0
right = n-1

each = num_list[left] + num_list[right]
cnt = 0
while left < right: # left == right 되면 break
    if each == x:
        cnt += 1
        each -= num_list[left]
        left += 1
        each += num_list[left]
    elif each < x:
        each -= num_list[left]
        left += 1
        each += num_list[left]
    else:
        each -= num_list[right]
        right -= 1
        each += num_list[right]
print(cnt)