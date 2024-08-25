N, X = map(int, input().split())
num_list = list(map(int, input().split()))

ret_list = []
for num in num_list:
    if (num < X):
        ret_list.append(num)

print(" ".join(map(str, ret_list)))