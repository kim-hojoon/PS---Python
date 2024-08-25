N = int(input())
ret = 0
for _ in range(N):
    word = str(input())
    word_set = set()
    last_a = word[0]
    ret += 1
    for a in word:
        if ((a in word_set) and (a != last_a)):
            ret -= 1
            break
        else:
            word_set.add(a)
            last_a=a
print(ret)