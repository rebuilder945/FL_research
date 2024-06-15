
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    for c in s1:
        d1[c] = d1.get(c, 0) + 1

    for c in s2:
        d2[c] = d2.get(c, 0) + 1

    return d1 == d2

s1 = input().strip()
s2 = input().strip()

if is_anagram(s1, s2):
    print('True')
else:
    print('False')

