N = int(input())
num_list = list(map(int, input().split()))

max_score = max(num_list)
new_list = [(n/max_score)*100 for n in num_list]

print(f"{sum(new_list)/len(new_list)}")