import sys
f = sys.stdin

n = int(f.readline())

worker_set = set()

for _ in range(n):
    name, enter_or_leave = map(str, f.readline().split())
    if enter_or_leave == "enter":
        worker_set.add(name)
    else:
        worker_set.remove(name)

worker_list = sorted(worker_set, reverse=True)

print("\n".join(worker_list))