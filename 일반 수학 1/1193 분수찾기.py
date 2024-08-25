n = int(input())

base = 1

while n > base:
    n -= base
    base += 1

if (base % 2 == 0):
    print(f"{n}/{base+1-n}")
else:
    print(f"{base+1-n}/{n}")