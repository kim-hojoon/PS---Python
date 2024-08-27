N, M = map(int, input().split())

A, B = [], []
for _ in range(N):
    temp_row = list(map(int, input().split()))
    A.append(temp_row)
for _ in range(N):
    temp_row = list(map(int, input().split()))
    B.append(temp_row)
sum = []
for (row_a, row_b) in zip(A, B):
    for (a, b) in zip(row_a, row_b):
        print(f"{a+b} ", end="")
    print("")