import sys
f = sys.stdin

a, b, c, d, e, f = map(int, f.readline().split())

div = b*d - a*e
x = (b*f - c*e) // div
y = (c*d - a*f) // div

print(f"{x} {y}")