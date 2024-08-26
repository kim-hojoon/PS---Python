import sys
f = sys.stdin

n = int(f.readline())

for _ in range(n):
    string = str(f.readline().strip())

    stack = 0
    for a in string:
        if a == "(":
            stack += 1
        elif a == ")":
            if (stack != 0):
                stack -= 1
            else:
                stack = -1
                break
    if stack == 0:
        print("YES")
    else:
        print("NO")