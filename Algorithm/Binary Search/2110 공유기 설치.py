"""
시간 복잡도
N : 2 x 10^5 => O(N logN) 이하
C : 2 ^ 10^5 => O(C logC) 이하

아이디어
1. 브루트 포스 (백트래킹) -> 모든 경우의수 nCc 로 공유기 최단 거리 구하기 -> 시간 초과
2. 이분탐색
    -> 공유기 사이의 최대 거리를 산정해두고, 해당 거리를 유지한채 총 몇 개의 공유기를 둘 수 있는지 계산할 수 있다
    -> start = 1, end = max로 설정해두고 mid라는 거리를 유지한 채 총 몇 개의 공유기를 둘 수 있는지 계산!
"""
import sys
f = sys.stdin

n, c = map(int, f.readline().split())
num_list = [int(f.readline()) for _ in range(n)]
num_list.sort()

def count_num(d):
    last_num = num_list[0]
    cnt = 1
    for i in range(1, len(num_list)):
        if num_list[i] - last_num >= d:
            last_num = num_list[i]
            cnt += 1
    return cnt

start, end = 1, (num_list[-1] - num_list[0])
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = count_num(mid)
    if cnt >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)