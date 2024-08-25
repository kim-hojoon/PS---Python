import sys
f = sys.stdin

num_list = list(str(f.readline().rstrip()))

num_list.sort(reverse=True)

print("".join(num_list))