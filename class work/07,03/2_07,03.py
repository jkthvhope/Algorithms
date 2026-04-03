def isAnagram(s, t):
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "cat"
print(isAnagram(s, t))


