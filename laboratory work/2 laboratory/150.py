# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = []
for i in tokens:
    if i == "+":
        result.append(result.pop() + result.pop())
    elif i == "-":
        b, a = result.pop(), result.pop()
        result.append(a - b)
    elif i == "*":
        result.append(result.pop() * result.pop())
    elif i == "/":
        b, a = result.pop(), result.pop()
        result.append(int(a / b))
    else:
        result.append(int(i))
print(result[0])
