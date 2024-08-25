import sys
f = sys.stdin

n, m = map(int, f.readline().split())

num_dict = { i : str(f.readline().strip()) for i in range(1,n+1) }
name_dict = { num_dict[i] : i for i in num_dict }

for _ in range(m):
    quiz = str(f.readline().strip())
    if (quiz.isnumeric()):
        print(num_dict[int(quiz)])
    else:
        print(name_dict[quiz])