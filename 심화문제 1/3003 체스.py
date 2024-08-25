num_list = list(map(int, input().split()))
right_num = [1, 1, 2, 2, 2, 8]

new_list = [ i - j for (i, j) in zip(right_num, num_list)]

print(" ".join(map(str, new_list)))