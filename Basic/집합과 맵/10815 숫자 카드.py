import sys
f = sys.stdin

n = int(f.readline())
deck_set = set(map(int, f.readline().split()))

m = int(f.readline())
num_list = list(map(int, f.readline().split()))

for num in num_list:
    if (num in deck_set):
        print("1 ", end="")
    else:
        print("0 ", end="")