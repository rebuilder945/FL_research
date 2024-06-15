def first_unique_char(s):
    if not s:
        return "None"
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in s:
        if freq[c] == 1:
            return c
    return "None"
n=input()
print(first_unique_char(n))

