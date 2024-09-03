"""
아이디어: -가 나온 뒤에 괄호 열기 ( -> 한번 더 -가 나오면 괄호 닫기
"""

import sys
f = sys.stdin

equation = str(f.readline().strip())

if "-" in equation:
    plus_list = equation.split("-")
else:
    plus_list = []
    plus_list.append(equation)

is_first = True
ans = 0

for plus_term in plus_list:
    if "+" in plus_term:
        temp_list = list(map(int, plus_term.split("+")))
        temp_sum = sum(temp_list)
    else:
        temp_sum = int(plus_term)

    if is_first:
        ans += temp_sum
        is_first = False
    else:
        ans -= temp_sum
print(ans)