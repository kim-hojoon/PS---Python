"""
아이디어
- 어차피 합의 최솟값만 출력하면 되기 때문에 A는 오름차순, B는 내림차순으로 정렬후 index 대로 곱하면 됨
"""

import sys
f = sys.stdin

n = int(f.readline())
A = list(map(int, f.readline().split()))
B = list(map(int, f.readline().split()))

A.sort()                # A 오름차순 정렬
B.sort(reverse=True)    # B 내림차순 정렬

ans = 0
for i in range(n):
    ans += A[i] * B[i]
print(ans)