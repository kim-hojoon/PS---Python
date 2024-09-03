"""
시간 복잡도
- N: 10^5 => O(N logN) 이하의 알고리즘 => 백트래킹은 불가능 (모든 경우의 수 다 찾는 것 불가능)

아이디어
- 길이가 짧은 회의를 최대한 넣을까?
- 빨리 끝나는 회의를 최대한 넣을까?
-> 힌트를 바탕으로 추론하면, 남은 것 중 끝나는 시간이 가장 빠른를 택한다 -> 해당 시간보다 빨리 시작하는 회의는 선택지에서 지운다. 반복!!
"""

import sys
f = sys.stdin

n = int(f.readline())
meeting_list = [ list(map(int, f.readline().split())) for _ in range(n) ]

meeting_list.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간이 빠른 순으로 정렬

cnt = 0
current_time = 0
for (start, end) in meeting_list:
    if start >= current_time:
        cnt += 1
        current_time = end
        # print(f"({start}, {end})")
print(cnt)