"""
시간복잡도
- n: 10^6 => O(n logn) 이하

아이디어
- 다이나믹 프로그래밍 => 1부터 점점 증가시키며 원하는 결과가 나올 때까지 값을 구함
-> O(n) 풀이
"""

import sys
f = sys.stdin

n = int(f.readline())

cnt_dict = {1:0, 2:1, 3:1}

for num in range(4, n+1):
    min_cnt = cnt_dict[num-1] + 1
    if num % 3 == 0:
        min_cnt = min(min_cnt, cnt_dict[num//3] + 1)  
    if num % 2 == 0:
        min_cnt = min(min_cnt, cnt_dict[num//2] + 1)
    cnt_dict[num] = min_cnt

print(cnt_dict[n])