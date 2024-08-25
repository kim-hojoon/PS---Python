a, b = map(str, input().split())

a_list = list(a)
b_list = list(b)

a_r = int("".join(reversed(a_list)))
b_r = int("".join(reversed(b_list)))

print(max([a_r, b_r]))