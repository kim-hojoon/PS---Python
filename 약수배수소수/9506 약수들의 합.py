N = int(input())
while (N != -1):
    factors = []
    for i in range(1, N):
        if (N % i == 0):
            factors.append(i)

    if (sum(factors) == N):
        sentence = " + ".join(map(str, factors))
        print(f"{N} = {sentence}")
    else:
        print(f"{N} is NOT perfect.")
    N = int(input())
