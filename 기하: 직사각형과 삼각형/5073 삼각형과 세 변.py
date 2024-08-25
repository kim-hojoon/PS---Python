import sys
f = sys.stdin

while True:
    a, b, c = map(int, f.readline().split())

    if (a == 0 and b == 0 and c == 0):
        break

    line_set = set([a, b, c])

    if (sum([a,b,c]) <= 2 * max([a,b,c])):
        print("Invalid")
    elif len(line_set) == 1:
        print("Equilateral")
    elif len(line_set) == 2:
        print("Isosceles")
    else:
        print("Scalene")