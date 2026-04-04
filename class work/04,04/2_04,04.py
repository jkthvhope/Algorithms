# 383
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}  # {буква : кол-во}
        for char in magazine:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
        for char in ransomNote:
            if char not in table or table[char] <= 0:
                return False
            table[char] -= 1
        return True
sol = Solution()
print(f'ransomNote = "a", magazine = "b" -> {sol.canConstruct("a", "b")}')
print(f'ransomNote = "aa", magazine = "ab" -> {sol.canConstruct("aa", "ab")}')
print(f'ransomNote = "aa", magazine = "aab" -> {sol.canConstruct("aa", "aab")}')