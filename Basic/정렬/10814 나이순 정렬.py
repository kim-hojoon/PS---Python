import sys
f = sys.stdin

n = int(f.readline())

database = [ tuple(map(str, f.readline().strip().split())) for _ in range(n)]

database.sort(key = lambda x: int(x[0]))

for age, name in database:
    print(f"{age} {name}")