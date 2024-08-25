import sys
f = sys.stdin

n = int(f.readline())

cor_list = []

for _ in range(n):
    (x, y) = map(int, f.readline().split())
    cor_list.append((y, x))

cor_list.sort()

for (y, x) in cor_list:
    print(f"{x} {y}")