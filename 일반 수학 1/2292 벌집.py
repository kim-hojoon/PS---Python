n = int(input())

if n == 1:
    print(1)

else:
    shell = 1
    n -= 1
    while (n > (6 * shell)):
        n -= (6 * shell)
        shell += 1
    print(shell+1)