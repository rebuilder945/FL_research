from collections import Counter

def first_unique_char(s):
    if not s:
        return "None"
    char_count = Counter(s)
    for c in s:
        if char_count[c] == 1:
            return c
    return "None"

input_str = input()
print(first_unique_char(input_str))
