"""
아이디어
    - 깊이가 정해져 있지 않음 -> 백트래킹 -> 재귀 함수가 m번 돌면 return
    - 백트래킹 과정 중 조건 추가
변수
    - cnt : m이 될 때 return
    - visited: bool[] 방문여부    
    - result: int[] -> result의 마지막 원소보다 큰지 확인
"""

import sys
f = sys.stdin

n, m = map(int, f.readline().split())
visited = [False for _ in range(n+1)]
result = []

def rec(cnt, last):
    if cnt == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(last+1, n+1):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            result.append(i)
            
            rec(cnt, i)

            visited[i] = False
            cnt -= 1
            result.pop()

rec(0, 0)