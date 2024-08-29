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
elif n == 2:
    print(1)
    exit()

# 소수 찾기 알고리즘
def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True

prime_list = []
for num in range(2, n+1):
    if is_prime(num):
        prime_list.append(num)

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