import sys
f = sys.stdin

n = int(f.readline())

num_list = []

for _ in range(n):
    num_list.append(int(f.readline()))

num_list.sort()

for num in num_list:
    print(num)