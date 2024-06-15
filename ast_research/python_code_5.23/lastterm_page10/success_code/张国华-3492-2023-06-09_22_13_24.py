s = input()
if not s:
    print("None")
else:
    hash_table = {}
    for c in s:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1
    for c in s:
        if hash_table[c] == 1:
            print(c)
            break
