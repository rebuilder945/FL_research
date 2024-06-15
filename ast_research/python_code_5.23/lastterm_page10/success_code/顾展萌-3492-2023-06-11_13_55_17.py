
def get_first_non_repeating_char(s):
    if not s:
        return "None"

    hash_table = {}
    for c in s:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1

    for c in s:
        if hash_table[c] == 1:
            return c

    return "None"

