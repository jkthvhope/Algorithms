# 735

# asteroids = [5,10,-5]
# asteroids = [8, -8]
# asteroids = [10,2,-5]

asteroids = [3, 5, -6, 2, -1, 4]
stack = []

for ast in asteroids:
    while stack and ast < 0 < stack[-1]:  # стек > 0, аcтероид < 0
        if stack[-1] < abs(ast):
            stack.pop()
            continue
        elif stack[-1] == abs(ast):
            stack.pop()
            break
        else:
            break
    else:
        stack.append(ast)

print(stack)