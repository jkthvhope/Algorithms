# 946

# pushed = [1,2,3,4,5]
# popped = [4,3,5,1,2]

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
stack = []
i = 0
for x in pushed:
    stack.append(x)
    while stack and stack[-1] == popped[i]:
        stack.pop()
        i += 1
print(len(stack) == 0)