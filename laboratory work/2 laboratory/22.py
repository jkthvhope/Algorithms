n = 3
result = []
stack = [(0, 0, '')]
while stack:
    l, r, s = stack.pop()
    if len(s) == n * 2:
        result.append(s)
        continue
    if l < n:
        stack.append((l + 1, r, s + '('))
    if r < l:
        stack.append((l, r + 1, s + ')'))
print(result)