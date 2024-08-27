def smallest_factor(n):
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return i
    return n

N = int(input())

while (N != 1):
    f = smallest_factor(N)
    print(f)
    N = N//f