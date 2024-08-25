grade_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

grade_list = []
total_credit = 0.0
total_mul = 0.0
for _ in range(20):
    name, credit, grade = list(map(str, input().split()))
    if (grade == "P"):
        pass
    else:
        total_credit += float(credit)
        total_mul += float(credit) * float(grade_dict[grade])

print(total_mul/total_credit)