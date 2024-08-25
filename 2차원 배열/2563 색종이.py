N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

paper_map = [[0 for _ in range(100)] for _ in range(100)]

for x0, y0 in papers:
    for i in range(10):
        for j in range(10):
            paper_map[x0+i][y0+j]=1
sum_list = [sum(l) for l in paper_map]

print(sum(sum_list))