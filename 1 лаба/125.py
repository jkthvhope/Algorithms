def is_palindrome(s):
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("race a car"))
# print(is_palindrome(" "))

"""left = 0
right = len(s) - 1
is_palindrome = True
while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    if s[left].lower() != s[right].lower():
        is_palindrome = False
        break
    left += 1
    right -= 1
print(is_palindrome)"""
