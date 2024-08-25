t = int(input())

coin_list = [25, 10, 5, 1]

for _ in range(t):
    money = int(input())
    answer_list = []
    for coin in coin_list:
        answer_list.append(money // coin)
        money = money % coin
    print(" ".join(map(str, answer_list)))