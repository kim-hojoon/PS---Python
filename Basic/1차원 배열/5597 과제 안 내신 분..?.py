num_list = [0 for _ in range(1, 31)]

for _ in range(28):
    num = int(input())
    num_list[num-1] = 1

i1 = num_list.index(0)
num_list[i1] = 1
i2 = num_list.index(0)

print(f"{i1+1}\n{i2+1}")