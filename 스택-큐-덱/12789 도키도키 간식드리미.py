import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))

stack = []
order = 1

is_nice = True

for num in num_list:
    # stack 상단 번호 모두 처리
    while (stack and stack[-1] == order):
        stack.pop()
        order += 1
    
    # stack 상단 처리 후 본인 확인
    if num == order:
        order += 1
    
    # stack 상단이 본인보다 작을 경우 Sad
    elif (stack and stack[-1] < num):
        is_nice = False
        break
    # stack이 비었거나 본인보다 큰 경우 push 후 continue
    else:
        stack.append(num)

if is_nice: print("Nice")
else: print("Sad")
