import sys
f = sys.stdin

num_list = []
for _ in range(5):
    num_list.append(int(f.readline()))
num_list.sort()

avg = sum(num_list) // 5
mid = num_list[2]

print(f"{avg}\n{mid}")