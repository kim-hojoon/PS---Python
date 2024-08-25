import sys
f = sys.stdin

n = int(f.readline())
holding_list = list(map(int, f.readline().split()))
m = int(f.readline())
check_list = list(map(int, f.readline().split()))

holding_dict = {}
for num in holding_list:
    if num in holding_dict:
        holding_dict[num] = holding_dict[num] + 1
    else:
        holding_dict[num] = 1

for num in check_list:
    if num in holding_dict:
        print(holding_dict[num], end=" ")
    else:
        print("0", end=" ")