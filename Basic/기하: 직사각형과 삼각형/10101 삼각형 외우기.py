import sys
f = sys.stdin

angle_list = []
for _ in range(3):
    angle_list.append(int(f.readline()))

if sum(angle_list) == 180:
    angle_set = set(angle_list)
    if len(angle_set)==1:
        print('Equilateral')
    elif len(angle_set)==2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')