import sys
sys.setrecursionlimit(1000000)
f = sys.stdin

n = int(f.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, f.readline().split())
    graph[u].append(v)
    graph[v].append(u)

parent_list = [0 for _ in range(n+1)]

def dfs(i):
    for ni in graph[i]:
        if parent_list[ni] == 0:
            parent_list[ni] = i
            dfs(ni)

parent_list[1] = -1
dfs(1)

print("\n".join(map(str, parent_list[2:])))
            