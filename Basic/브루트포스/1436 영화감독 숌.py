import sys
f = sys.stdin

n = int(f.readline())

num = 666
cnt = 0

while True:
    if ("666" in str(num)):
        cnt += 1
    if (cnt == n):
        break
    num += 1
print(num)