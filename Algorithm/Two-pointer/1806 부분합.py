import sys
f = sys.stdin
INF = sys.maxsize

n, s = map(int, f.readline().split())
num_list = list(map(int, f.readline().split()))

minv = INF

head = 0 # 추가할 index
tail = 0 # 뺄 index
res = 0

while True:
    if res < s:
        if head == n: # 합계 부족 but 끝 도착
            break
        res += num_list[head]
        head += 1
    else:
        minv = min(minv, head - tail)
        res -= num_list[tail]
        tail += 1
        if head <= tail:
            break

if minv == INF : print(0)
else: print(minv)