num_set = set()

for _ in range(10):
    num = int(input())
    rem = num % 42
    num_set.add(rem)

print(len(num_set))