"""
1. 아이디어
    - 순열: 총 몇 개, 즉 깊이가 정해져있음! M으로
    - 사전 순으로 나열 -> 재귀함수로 하나씩 돌면 됨 (넣었다 빼기)

2. 시간 복잡도
    - 중복 없으므로 O(N!)

3. 변수
    - 결과 리스트: int[]
    - 방문 여부 리스트 : bool[]

"""

import sys
f = sys.stdin

n, m = map(int, f.readline().split())

visited = [False for _ in range(n+1)]
result = []

def rec(cnt):
    if cnt == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            cnt += 1

            rec(cnt)

            visited[i] = False
            result.pop()
            cnt -= 1
rec(0)