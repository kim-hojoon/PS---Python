word = str(input())
alpha_dict = dict()

for a in word:
    a = a.capitalize()
    if (a in alpha_dict):
        alpha_dict[a] += 1
    else:
        alpha_dict[a] = 1

max_v = 0
most_alpha = ""

for (k, v) in alpha_dict.items():
    if (v > max_v):
        most_alpha = k
        max_v = v
    elif (v == max_v):
        most_alpha = "?"

print(most_alpha)