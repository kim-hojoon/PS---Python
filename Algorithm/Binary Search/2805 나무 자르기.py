"""
시간 복잡도
N = 10^6 -> O(nlogn) 이하의 알고리즘
M = 2 x 10^9 -> O(m) 이하의 알고리즘

아이디어
- 이분탐색은 정렬된 리스트의 인덱스를 기준으로만 할 수 있는 게 아니다!
- 특정 범위 내에서 원하는 값을 구하려 할 때, min과 max의 mid를 기준으로 이분 탐색이 가능하다
-> mid의 값이 정도일 때, 결과가 어떻게 되지?
    -> 결과보다 작구나! 그러면 mid와 min 사이에 답이 있겠네
    -> 결과보다 크구나! 그러면 mid와 max 사이에 답이 있겠네
""" 

import sys
from math import ceil
f = sys.stdin

n, m = map(int, f.readline().split())
num_list = list(map(int, f.readline().split()))

start, end = 1, max(num_list)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for height in num_list:
        if height > mid:
            total += height - mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)