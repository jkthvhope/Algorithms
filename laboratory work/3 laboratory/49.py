def groupAnagrams(strs):
    anagram = {}
    for i in strs:
        sorted_word = "".join(sorted(i))
        if sorted_word not in anagram:
            anagram[sorted_word] = []
        anagram[sorted_word].append(i)
    return list(anagram.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

# strs = ["tan", "nat"]
