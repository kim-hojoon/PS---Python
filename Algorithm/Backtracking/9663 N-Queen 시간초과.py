"""
아이디어
- 브루트포스 : NxN 체스판 위에 퀸을 3마리 두고 서로 공격 가능한지 체크해본다. -> 공격 불가 하면 cnt += 1
- 백트래킹 : 체스판 위에 퀸을 3개 두는 방법 -> 재귀 함수 3번으로 가능

변수
- ans: int 총 가능한 경우의 수

"""

import sys
f = sys.stdin

n = int(f.readline())

ans = 0

def is_possible(index):
    y = index // n
    x = index % n

    if not queen_list:
        return True

    for queen_index in queen_list:
        q_y, q_x = queen_index // n, queen_index % n
        if (x == q_x) or (y == q_y) or (x + y == q_x + q_y) or (x - y == q_x - q_y):
            return False
    return True

queen_list = []

def rec(cnt, last_index):
    global ans
    if cnt == n:
        ans += 1
        return
    for index in range(last_index+1, n**2):
        if not is_possible(index):
            continue       
        queen_list.append(index)
        cnt += 1
        rec(cnt, index)
        queen_list.pop()
        cnt -= 1
                
rec(0, -1)

print(ans)