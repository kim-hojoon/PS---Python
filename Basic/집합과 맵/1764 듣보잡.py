import sys
f = sys.stdin

n, m = map(int, f.readline().split())
no_listen = set(str(f.readline().strip()) for _ in range(n))
no_see = set(str(f.readline().strip()) for _ in range(m))

no_l_s = no_listen.intersection(no_see)
name_list = sorted(no_l_s)

print(len(name_list))
print("\n".join(name_list))