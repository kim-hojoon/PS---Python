import sys
f = sys.stdin

n = int(f.readline())

result = 0

for i in range(1, n):
    temp = i + sum(map(int, list(str(i))))
    if n == temp:
        result = i
        break

print(result)