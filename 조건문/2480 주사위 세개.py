x, y, z = map(int, input().split())
num_same = 0
dup_num = 0
ret = 0
if (x==y):
    num_same += 1
    dup_num = x
if (y==z):
    num_same += 1
    dup_num = y
if (z==x):
    num_same += 1
    dup_num = z

if (num_same == 0):
    ret = max([x,y,z])*100
elif (num_same == 1):
    l1 = [x, y, z]
    ret = 1000 + (dup_num * 100)
else:
    ret = 10000 + (dup_num * 1000)

print(ret)