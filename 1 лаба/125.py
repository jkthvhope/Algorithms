def is_palindrome(s):
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("race a car"))
# print(is_palindrome(" "))
