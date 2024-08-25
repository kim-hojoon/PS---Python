N, M = map(int, input().split())

basket_list = [i for i in range(1,N+1)]

for _ in range(M):
    n1, n2  = map(int, input().split())
    n1 -= 1
    n2 -= 1
    v1, v2 = basket_list[n1], basket_list[n2]
    basket_list[n1] = v2
    basket_list[n2] = v1

print(" ".join(map(str,basket_list)))