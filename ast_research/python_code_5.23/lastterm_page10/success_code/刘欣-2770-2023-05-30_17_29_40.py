str1 = input().strip()
str2 = input().strip()

if len(str1) != len(str2):
    print(False)
else:
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                print(False)
                break
        else:
            print(False)
            break
    else:
        print(True)
