n = int(input())

row_num = 1
points = 4

for i in range(1,n+1):
    points += 5 * (row_num**2)
    points -= 2 * (row_num**2 - row_num)

    row_num *= 2

print(points)