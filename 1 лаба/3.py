# s = "bbbbb"
# s = "pwwkew"
s = "abcabcbb"
window = ""
max_len = 0
for char in s:
    if char in window:
        char_index = window.find(char)
        window = window[char_index + 1:]
    window += char
    if len(window) > max_len:
        max_len = len(window)
print(max_len)