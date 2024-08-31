"""
시간 복잡도
N = 10**5 => O(nlogn)으로 풀어라
M = 10**5

수 찾기 -> 정렬 후 Binary Search!
- N 정렬하기 -> n logn
- M 번 Binary Search -> m * logn
=> 가능!

"""

import sys
f = sys.stdin

n = int(f.readline())
num_list = list(map(int, f.readline().split()))
m = int(f.readline())
query_list = list(map(int, f.readline().split()))

num_list.sort()

def binary_search(start, end, query):
    mid = (start + end) // 2
    midv = num_list[mid]

    if start == end:    # 원소가 하나 남았을 때 -> 마지막 search
        if midv == query:
            return 1
        else:
            return 0
    elif query < midv:  # query가 더 작을 때 -> 왼쪽에서 다시
        return binary_search(start, mid-1, query)
    else:               # query가 크거나 같을 때 -> 오른쪽에서 다시
        return binary_search(mid, end, query)

for query in query_list:
    print(binary_search(0, n-1, query))