word = str(input())

alpha_list = "abcdefghijklmnopqrstuvwxyz"
for a in alpha_list:
    if a in word:
        print(word.index(a), end=" ")
    else:
        print(-1, end=" ")