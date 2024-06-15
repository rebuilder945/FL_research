
from collections import Counter

def get_first_non_repeating_char(s):
    if not s:
        return "None"

    counter = Counter(s)
    for c in s:
        if counter[c] == 1:
            return c

    return "None"

