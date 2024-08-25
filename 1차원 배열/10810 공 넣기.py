N, M = map(int, input().split())

basket_list = [0 for _ in range(N)]

for _ in range(M):
    s, e, n  = map(int, input().split())
    basket_list[s-1:e] = [n] * (e-s+1)

print(" ".join(map(str,basket_list)))