N, M = map(int, input().split())
basket = [i for i in range(1,N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    portion = basket[i-1:j]
    portion.reverse()
    basket[i-1:j] = portion

print(" ".join(map(str, basket)))