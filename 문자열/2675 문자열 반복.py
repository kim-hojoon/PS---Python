n = int(input())

for _ in range(n):
    t, word = map(str, input().split())
    t = int(t)
    for a in word:
        repeat_a = a * t
        print(repeat_a, end="")
    print("")