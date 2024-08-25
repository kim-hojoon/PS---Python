import sys
f = sys.stdin

n, m = map(int, f.readline().split())

key_words = set([str(f.readline().strip()) for _ in range(n)])
cnt = 0

for _ in range(m):
    word = str(f.readline().strip())
    if word in key_words:
        cnt += 1
print(cnt)