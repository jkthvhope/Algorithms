# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([])"
s = "([)]"
brackets = {")": "(", "}": "{", "]": "["}
stack = []
flag = True
for i in s:
    if i in brackets: # смотрим ключ
        if stack:
            last_element = stack.pop()
            if brackets[i] != last_element:
                flag = False
                break
        else:
            flag = False
            break
    else:
        stack.append(i)
if flag and len(stack) == 0:
    print(True)
else:
    print(False)