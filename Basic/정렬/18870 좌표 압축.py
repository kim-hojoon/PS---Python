import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))

num_set = sorted(list(set(num_list)))

num_dict = {}
for i in range(len(num_set)):
    num = num_set[i]
    num_dict[num] = i

for num in num_list:
    print(num_dict[num], end=" ")