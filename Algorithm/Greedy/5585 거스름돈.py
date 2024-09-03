import sys
f = sys.stdin

money = int(f.readline())

coin_list = [500, 100, 50, 10, 5 , 1]

remainder = 1000 - money    # 받아야 할 돈
cnt = 0                     # 총 받을 동전 개수
for coin in coin_list:
    if remainder == 0:
        break
    cnt += remainder // coin
    remainder = remainder % coin
print(cnt)