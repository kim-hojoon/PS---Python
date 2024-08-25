import sys
f = sys.stdin

x, y, w, h = map(int, f.readline().split())
d_list = [x, y, (w-x), (h-y)]

print(min(d_list))