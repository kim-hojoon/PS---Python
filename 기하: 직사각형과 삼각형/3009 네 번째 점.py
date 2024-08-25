import sys
f = sys.stdin

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, f.readline().split())
    x_list.append(x)
    y_list.append(y)

x_set = set(x_list)
y_set = set(y_list)

print(f"{2*sum(x_set) - sum(x_list)} {2*sum(y_set) - sum(y_list)}")