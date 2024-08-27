def is_prime(n):
    factors = []
    for i in range(1,n):
        if (n % i == 0):
            factors.append(i)
    if (len(factors) == 1):
        return True
    else:
        return False

N = int(input())

num_list = list(map(int, input().split()))
result = 0
for num in num_list:
    if (is_prime(num)):
        result += 1

print(result)