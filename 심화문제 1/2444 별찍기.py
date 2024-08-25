N = int(input())
total_len = 2*N-1
for i in range(1,N+1):
    num_star = 2*i-1
    space_len = (total_len - num_star) // 2
    print(" "*space_len, end = "")
    print("*"*num_star, end = "\n")
for i in range(N-1,0,-1):
    num_star = 2*i-1
    space_len = (total_len - num_star) // 2
    print(" "*space_len, end = "")
    print("*"*num_star, end = "\n")