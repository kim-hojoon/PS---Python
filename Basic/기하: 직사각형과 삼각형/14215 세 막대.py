import sys
f = sys.stdin

a, b, c = map(int, f.readline().split())
line_list = [a, b, c]

answer = 0
if (sum(line_list) > 2 * max(line_list)):
    answer = sum(line_list)
else:
    answer = 2 * (sum(line_list) - max(line_list)) - 1
print(answer)