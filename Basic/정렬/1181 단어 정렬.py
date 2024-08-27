# import sys
# f = sys.stdin

# n = int(f.readline())

# words_by_len = [ [] for _ in range(51)]

# for _ in range(n):
#     word = str(f.readline().rstrip())
#     w_len = len(word)
#     if word in words_by_len[w_len]:
#         continue
#     else:
#         words_by_len[w_len].append(word)

# for w_list in words_by_len:
#     if len(w_list) != 0:
#         for word in sorted(w_list):
#             print(word)

import sys
f = sys.stdin

n = int(f.readline())

words = [str(f.readline().rstrip()) for _ in range(n)]
words = list(set(words))

words.sort(key = lambda x: (len(x), x))

print("\n".join(words))