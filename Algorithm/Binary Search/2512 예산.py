"""
시간 복잡도
N: 10^5 -> O(N logN) 이하

아이디어
최대 upper bound 설정? -> 나무 자르기 문제와 동일!
    - 예산 upper bound를 설정하면 linear 순회를 통해 총 사용 예산을 알 수 있게 된다
        -> 총 사용 예산이 total보다 크면 upper bound를 줄이고
        -> total보다 작거나 같으면 upper bound를 늘린다
    이분 탐색을 통해 upper bound를 구한다!
"""
import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))
total = int(f.readline())

def cal_amount(upper_bound):
    amount = 0
    for num in num_list:
        if num >= upper_bound:
            amount += upper_bound
        else:
            amount += num
    return amount

start, end = 0, max(num_list)
ans = 0

while start <= end:
    mid = (start + end) // 2
    amount = cal_amount(mid)
    if amount > total:  # 크면 예산을 줄여야한다
        end = mid -1
    else:               # 작거나 같으면 예산을 늘려야한다
        ans = mid
        start = mid + 1
print(ans)