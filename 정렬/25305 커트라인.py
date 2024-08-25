import sys
f = sys.stdin

n, k = map(int, f.readline().split())
score_list = list(map(int, f.readline().split()))
score_list.sort(reverse=True)

print(score_list[k-1])