# 387
def firstUniqChar(s: str) -> int:
    table = {}  # {буква : [кол-во,1-ый индекс]}
    for i in range(len(s)):
        char = s[i]
        if char not in table:
            table[char] = [1, i]
        else:
            table[char][0] += 1
    for char in table:
        count, index = table[char]
        if count == 1:
            return index
    return -1
print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))
print(firstUniqChar('aabb'))
