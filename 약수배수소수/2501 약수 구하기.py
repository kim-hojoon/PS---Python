N, K = map(int, input().split())

factors = []

for i in range(1, N+1):
    if (N % i == 0):
        factors.append(i)

if (K <= len(factors)):
    print(factors[K-1])
else:
    print("0")