import sys
f = sys.stdin

n = int(f.readline())

col_list = [False for _ in range(n)]
queen_list = []

def is_possible(y, x):
    if not queen_list:
        return True
    for qy, qx in queen_list:
        if (x + y == qx + qy) or (x - y == qx - qy):
            return False
    return True

ans = 0
def rec(y):
    global ans
    if y == n:
        ans += 1
        return

    for x in range(n):
        if not col_list[x] and is_possible(y, x):
            col_list[x] = True
            queen_list.append((y, x))
            rec(y+1)
            col_list[x] = False
            queen_list.pop()

rec(0)
print(ans)