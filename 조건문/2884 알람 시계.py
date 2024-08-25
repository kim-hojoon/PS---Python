h, m = map(int, input().split())

if (m>=45):
    print(f"{h} {m-45}")
else:
    m_new = m + 15
    h_new = h - 1
    if (h == 0):
        h_new = 23
    print(f"{h_new} {m_new}")