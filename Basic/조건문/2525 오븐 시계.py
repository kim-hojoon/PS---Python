h, m = map(int, input().split())
remain = int(input())

h_delta = remain // 60
m_delta = remain % 60

h_ret = h + h_delta
m_ret = m + m_delta

if (m_ret >= 60):
    h_ret += 1
    m_ret -= 60
if (h_ret >= 24):
    h_ret -= 24

print(f"{h_ret} {m_ret}")