string = input()
if string == "":
    print("None")
else:
    hash_table = {}
    for char in string:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    for char in string:
        if hash_table[char] == 1:
            print(char)
            break
    else:
        print("None")
