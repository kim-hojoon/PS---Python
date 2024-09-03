"""
아이디어: 다이나믹 프로그래밍 (점화식)
하나씩 해보기!
    1   =   1가지
    2   =   2가지
    3   =   3가지
    a_n = a_(n-1) + a_(n)
"""
import sys
f = sys.stdin

n = int(f.readline())

res_list = [0, 1, 2]

for num in range(3, n+1):
    a = res_list[num-1]
    b = res_list[num-2]
    res_list.append((a + b) % 10007)

print(res_list[n])