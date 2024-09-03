"""
아이디어: 그리디 -> A_i는 A_i-1의 배수라는 조건 때문에 무조건 비싼 동전을 최대한 많이 쓰는 게 유리하다
"""

import sys
f = sys.stdin

n, k = map(int, f.readline().split())

coin_list = [ int(f.readline()) for _ in range(n) ]
coin_list.reverse()

cnt = 0
remainder = k
for coin in coin_list:
    if remainder != 0:
        cnt += remainder // coin
        remainder = remainder % coin
print(cnt)