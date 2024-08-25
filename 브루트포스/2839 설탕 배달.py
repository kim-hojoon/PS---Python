import sys
f = sys.stdin
n = int(f.readline())

if n % 5 == 0 :
    print(n // 5)
else:
    cnt = 0
    while n > 0:
        n -= 3
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(cnt)
            break