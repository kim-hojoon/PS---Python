import sys
f = sys.stdin

while True:
    sentence = str(f.readline().rstrip())
    if sentence == ".":
        break

    stack = []
    
    is_ok = True
    for a in sentence:
        if a == "(":
            stack.append(1)
        elif a == ")":
            if (stack and stack[-1] == 1):
                stack.pop()
            else:
                is_ok = False
                break
        elif a == "[":
            stack.append(2)
        elif a == "]":
            if (stack and stack[-1] == 2):
                stack.pop()
            else:
                is_ok = False
                break

    if stack : is_ok = False

    if is_ok: print("yes")
    else: print("no")