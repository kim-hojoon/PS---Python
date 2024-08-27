a, b, v = map(int, input().split())

days = 1
v -= a
unit_step = a-b

days += v // unit_step 
if (v % unit_step != 0):
    days += 1

print(days)