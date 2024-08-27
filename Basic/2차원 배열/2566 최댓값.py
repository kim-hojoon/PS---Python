table = [list(map(int, input().split())) for _ in range(9)]

max_i, max_j= 1, 1
max_v = -1
for i in range(9):
    for j in range(9):
        if (table[i][j] >= max_v):
            max_i = i+1
            max_j = j+1
            max_v = table[i][j]

print(f"{max_v}\n{max_i} {max_j}")