A,B,C = input().split()
x,y,z = int(A), int(B), int(C)
print(f"{(x+y)%z}\n{((x%z) + (y%z))%z}\n{(x*y)%z}\n{((x%z) * (y%z))%z}\n")