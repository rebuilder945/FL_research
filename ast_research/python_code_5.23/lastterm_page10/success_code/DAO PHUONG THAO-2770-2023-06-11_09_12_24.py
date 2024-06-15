def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    chars1 = sorted(list(str1))
    chars2 = sorted(list(str2))

    return chars1 == chars2

str1 = input()
str2 = input()

result = is_anagram(str1, str2)
print(result)



