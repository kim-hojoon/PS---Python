# max_v = 0
# max_i = 0
# for i in range(1,10):
#     value = int(input())
#     if (max_v < value):
#         max_v = value
#         max_i = i
# print(f"{max_v}\n{max_i}")

num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)) + 1)