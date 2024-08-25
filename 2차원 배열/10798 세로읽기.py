word_list = [list(map(str, input())) for _ in range(5)]

length_list = []
for word in word_list:
    length_list.append(len(word))

l = max(length_list)

for i in range(5):
    delta = l - length_list[i]
    for j in range(delta):
        word_list[i].append("")

for j in range(l):
    for i in range(5):
        print(word_list[i][j], end="")