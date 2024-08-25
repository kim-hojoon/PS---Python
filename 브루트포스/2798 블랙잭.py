import sys
f = sys.stdin

n, m = map(int, f.readline().split())
num_list = list(map(int, f.readline().split()))

max = -1

for i in range(0,n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp_sum = num_list[i] + num_list[j] + num_list[k]
            if (temp_sum <= m and temp_sum > max):
                max = temp_sum
print(max)