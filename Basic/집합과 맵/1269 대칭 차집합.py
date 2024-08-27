import sys
f = sys.stdin

n, m = map(int, f.readline().split())
set_a = set(map(int, f.readline().split()))
set_b = set(map(int, f.readline().split()))

inter_set = set_a.intersection(set_b)

answer = len(set_a) + len(set_b) - (2 * len(inter_set))
print(answer)