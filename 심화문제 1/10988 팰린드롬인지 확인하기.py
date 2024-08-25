# word = str(input())

# i = 0
# j = len(word) - 1

# ret = 1

# while (i<j):
#     if (word[i] == word[j]):
#         i += 1
#         j -= 1
#     else:
#         ret = 0
#         break
# print(ret)

word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)