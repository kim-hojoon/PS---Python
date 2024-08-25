A, B = input(), input()
x, y = int(A), int(B)

print(f"{x * (y%10)}\n{x * ((y // 10) % 10)}\n{x * (y // 100)}\n{x*y}")