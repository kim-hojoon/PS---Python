"""
아이디어: DP 가능 -> 2가지 최댓값 가능성
1. (index - 2에서의 최댓값) + (본인값) 
2. (index - 3에서의 최댓값) + (앞놈 값) + (본인값)

"""

import sys
f = sys.stdin

n = int(f.readline())
score_list = [0] + [ int(f.readline()) for _ in range(n) ]

if (n==1):
    print(score_list[1])
elif (n==2):
    print(score_list[1] + score_list[2])
else:
    max_list = [0] # 시작점의 최대값은 0점
    max_list.append(score_list[1]) # 첫번째 계단은 본인이 최대값
    max_list.append(score_list[1] + score_list[2]) # 두번째 계단은 두개 합친 게 최대값

    for i in range(3, n+1):
        v1 = max_list[i-2] + score_list[i]
        v2 = max_list[i-3] + score_list[i-1] + score_list[i]
        max_list.append(max(v1, v2))

    print(max_list[n])