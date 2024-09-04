"""
모든 점에서 모든 점에 대한 경로 찾기? -> 플로이드 워셜 문제

추가된 조건
- 본인에서 본인으로 갈 수 있는지 장담 X
- 경유지를 통해 가는 것이 더 비용이 적은가를 보는 것이 아닌, 경유지를 통해 가는 것이 가능한가를 본다!

자료구조
- 거리 리스트 (input으로 받은 것을 그대로 사용)

구현
- 삼중 for문을 돌면서 (경시끝)
    - 경유지를 통해가는 경로가 존재하면 시작과 끝점 사이가 이어진다고 표시 (1로 표시)
"""

import sys
f = sys.stdin

n = int(f.readline())

dist = [ list(map(int, f.readline().split())) for _ in range(n) ] # 0번부터 n-1번까지

for k in range(n): # 경
    for i in range(n): # 시
        for j in range(n): #끝
            if dist[i][k] == 1 and dist[k][j] == 1:
                dist[i][j] = 1

for row in dist:
    print(" ".join(map(str, row)))