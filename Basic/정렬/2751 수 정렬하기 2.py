import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readlines()))

num_list.sort()

print("\n".join(map(str, num_list)))