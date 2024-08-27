def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True

M = int(input())
N = int(input())

prime_list = []

for num in range(M,N+1):
    if (is_prime(num)):
        prime_list.append(num)

if (len(prime_list)==0):
    print(-1)
else:
    print(f"{sum(prime_list)}\n{prime_list[0]}")