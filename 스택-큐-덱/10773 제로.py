import sys
f = sys.stdin

k = int(f.readline())

stack = []

for _ in range(k):
    num = int(f.readline())
    if (num == 0):
        stack.pop()
    else:
        stack.append(num)
        
print(sum(stack))