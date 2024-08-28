# import sys
# sys.setrecursionlimit(10**9)
# f = sys.stdin

# r, c = map(int, f.readline().split())
# alpha_map = [list(f.readline().strip()) for _ in range(r)]

# dy, dx = [1,-1,0,0], [0,0,1,-1]

# cnt = 1

# def dfs(y, x, visited_alpha, local_cnt):
#     global cnt
#     local_cnt += 1
#     cnt = max(cnt, local_cnt)

#     for k in range(4):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if (0<=nx<c) and (0<=ny<r) and not (alpha_map[ny][nx] in visited_alpha):
#             visited_alpha.add(alpha_map[ny][nx])
#             dfs(ny, nx, visited_alpha, local_cnt)
#             visited_alpha.remove(alpha_map[ny][nx])


# dfs(0, 0, set(alpha_map[0][0]), 0)

# print(cnt)

"""
시간 초과

Python3와 PyPy3의 차이점 인지
간단한 코드        -> Python3가 메모리, 속도 측면에서 우세
복잡한 코드(반복)   -> PyPy3가 우세

이 문제의 경우,
DFS는 Python3로 통과할 수 없음 (PyPy3로는 가능)
BFS는 list, deque가 아닌 set을 이용해야 통과 가능

"""