import sys
f = sys.stdin

n = int(f.readline())

x_set = set()
y_set = set()

for _ in range(n):
    x, y = map(int, f.readline().split())
    x_set.add(x)
    y_set.add(y)

w = max(x_set) - min(x_set)
h = max(y_set) - min(y_set)

print(w*h)