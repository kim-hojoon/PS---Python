import sys
f = sys.stdin

n, m = map(int, f.readline().split())

result = []

def rec(cnt):
    if cnt == m:
        print(" ".join(map(str, result)))
        return
    for i in range(1, n+1):
        cnt += 1
        result.append(i)
        rec(cnt)
        cnt -= 1
        result.pop()

rec(0)