"""
연속된 수의 합 -> Two pointer 문제
n 이하의 모든 소수 구하기 -> 소수 구하기 알고리즘
"""

import sys
f = sys.stdin

n = int(f.readline())

if n == 1:
    print(0)
    exit()

# 소수 찾기 알고리즘
is_prime = [True for _ in range(n+1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(2*i, n+1, i):
            is_prime[j] = False

prime_list = [i for i in range(2, n+1) if is_prime[i] == True]

right = 1    # 앞으로 더할 값의 index
left = 0   # 앞으로 뺄 값의 index

res = prime_list[0]
cnt = 0
while True:
    if res == n:
        cnt += 1
        if right == len(prime_list):
            break
        res += prime_list[right]
        right += 1
    elif res < n:
        if right == len(prime_list):
            break
        res += prime_list[right]
        right += 1
    else:
        res -= prime_list[left]
        left += 1
print(cnt)