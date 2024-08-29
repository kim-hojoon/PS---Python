"""
아이디어 - 모든 경우의 수 계산? -> 백트래킹

변수 
- operators: 연산자 개수 담은 list
    -> 연산자 하나씩 꺼내면서 재귀 함수 호출 
"""

import sys
sys.setrecursionlimit(100000)
f = sys.stdin
INF = sys.maxsize

n = int(f.readline())
num_list = list(map(int, f.readline().split()))
operators = list(map(int, f.readline().split()))

maxv = - INF
minv = INF

ans = num_list[0]

def cal(operator, a, b):
    if operator == 0: # +
        return a + b
    elif operator == 1: # -
        return a - b
    elif operator == 2: # *
        return a * b
    elif operator == 3: # //
        if a < 0 and b > 0:
            return -(abs(a) // b)
        else:
            return a // b

def rec(cnt):
    global ans, maxv, minv
    if cnt == n-1:
        maxv = max(maxv, ans)
        minv = min(minv, ans)
        return
    for i in range(4):
        if operators[i] != 0:
            cnt += 1 
            operators[i] -= 1
            backup = ans
            ans = cal(i, ans, num_list[cnt])
            rec(cnt)
            cnt -= 1
            operators[i] += 1
            ans = backup

rec(0)
print(maxv)
print(minv)