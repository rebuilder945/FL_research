def first_unique_char(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s:
        if d[c] == 1:
            return c
    return None


s = input()
print(first_unique_char(s))
