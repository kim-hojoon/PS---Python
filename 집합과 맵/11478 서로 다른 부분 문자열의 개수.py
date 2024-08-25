import sys
f = sys.stdin

word = str(f.readline().strip())

snippet_set = set()

for length in range(1, len(word)+1):
    for index in range(0, len(word) - length + 1):
        snippet = word[index:index+length]
        snippet_set.add(snippet)
print(len(snippet_set))
