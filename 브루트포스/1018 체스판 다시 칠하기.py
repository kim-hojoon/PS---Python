import sys
f = sys.stdin

# board1 = ([list("WBWBWBWBWB")] + [list("BWBWBWBWBW")]) * 4
# board2 = ([list("BWBWBWBWBW")] + [list("WBWBWBWBWB")]) * 4

def count_chess(board):
    cnt1 = 0
    cnt2 = 0
    for i, row in enumerate(board):
        for j, e in enumerate(row):
            if ((i+j) % 2 == 0):
                if (e == "W"):
                    cnt1 +=1
                else:
                    cnt2 +=1
            else:
                if (e == "B"):
                    cnt1 +=1
                else:
                    cnt2 +=1
    return(min([cnt1, cnt2]))

n, m = map(int, f.readline().split())

board_list = []
for _ in range(n):
    board_list.append((list(f.readline().strip())))

answer = 64
for i in range(0, n-7):
    for j in range(0, m-7):
        temp_board = []
        for row in board_list[i:i+8]:
            temp_board.append(row[j:j+8])
        cnt = count_chess(temp_board)
        answer = min(answer, cnt)

print(answer)