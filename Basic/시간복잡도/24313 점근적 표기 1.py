import sys
f = sys.stdin

m, y_0 = map(int, f.readline().split())
c = int(f.readline())
x_0 = int(f.readline())

if (c < m) or ((m * x_0 + y_0) > c * x_0):
    print("0")
else:
    print("1")