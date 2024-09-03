"""
0 <= n <= 40

아이디어: 다이나믹 프로그래밍
    -> fb(3)은 결국 fb(2)와 fb(1)을 호출하기 때문에 fb(2)의 값 + fb(1)의 값을 합치면 된다
"""

import sys
f = sys.stdin

t = int(f.readline())
test_list = [ int(f.readline()) for _ in range(t) ]

res_list = []
res_list.append((1, 0)) # 0은 0 1번, 1 0번 호출
res_list.append((0, 1)) # 1은 0 0번, 1 1번 호출

for num in range(2, 41):
    zero_1, one_1 = res_list[num-1]
    zero_2, one_2 = res_list[num-2]
    res_list.append((zero_1+zero_2, one_1+one_2))

for test in test_list:
    zero, one = res_list[test]
    print(f"{zero} {one}")