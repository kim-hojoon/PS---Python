"""
시간 복잡도
- K: 10^4 => O (k^2) 이하
- N: 10^6 => O (n logn) 이하

아이디어
- 특정한 범위 내에서 원하는 결과를 찾는 것? -> 나무자르기 문제의 이분 탐색
- start = 1, k개 중 큰 것을 end로 두고 mid 일 때의 총 개수를 계산하자
    -> mid일 때의 총 개수가 N보다 작으면 -> mid가 더 작아져야한다 -> end = mid - 1로 설정
    -> mid일 때의 총 개수가 N보다 크거나 같으면 -> mid가 더 커질 수 있다 -> start = mid + 1로 설정
"""
import sys
f = sys.stdin

k, n = map(int, f.readline().split())
num_list = [ int(f.readline()) for _ in range(k) ]

start, end = 1, max(num_list)
ans = 0

def cal(mid):
    cnt = 0
    for num in num_list:
        cnt += (num // mid)
    return cnt

while start <= end:
    mid = (start + end) // 2
    cnt = cal(mid)

    if cnt >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)