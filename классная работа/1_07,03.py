def sortedSquarters(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[left]**2, s[right]**2
        left += 1
        right -= 1
    return sorted(s)

s = [-4,-1,0,3,10]
print(sortedSquarters(s))
