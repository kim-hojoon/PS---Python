import sys
f = sys.stdin

n = int(f.readline())

print(f"{n*(n-1)*(n-2)//6}\n3")

### i,j,k 값을 고르는 것을 nC3로 생각할 수 있음
### nC3을 계산해보면 n*(n-1)*(n-2) // 3*2