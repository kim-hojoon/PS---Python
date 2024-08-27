import sys
f = sys.stdin

n = int(f.readline())

cor_list = []

for _ in range(n):
    (x, y) = map(int, f.readline().split())
    cor_list.append((x, y))

cor_list.sort()

for (x, y) in cor_list:
    print(f"{x} {y}")

###########################################

# import sys
# input = sys.stdin.readline

# n = int(input())
# ls = []
# for _ in range(n):
#   ls.append(list(map(int, input().split())))

# for i in sorted(ls, key=lambda x: (x[0], x[1])):
#   print(i[0], i[1])