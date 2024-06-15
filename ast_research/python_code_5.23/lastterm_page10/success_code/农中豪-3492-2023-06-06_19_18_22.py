def find(s):
    if not s:
        return "None"
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for c in s:
        if char_count[c] == 1:
            return c
    print(char_count)
    return "None"
s = input()
print(find(s))
