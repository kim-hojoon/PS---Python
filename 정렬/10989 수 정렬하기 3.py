import sys
f = sys.stdin

n = int(f.readline())
num_dict = {}

for _ in range(n):
    num = int(f.readline())
    if num in num_dict:
        num_dict[num] = num_dict[num] + 1
    else:
        num_dict[num] = 1

for num, cnt in sorted(num_dict.items()):
    if (cnt != 0):
        for _ in range(cnt):
            print(num)