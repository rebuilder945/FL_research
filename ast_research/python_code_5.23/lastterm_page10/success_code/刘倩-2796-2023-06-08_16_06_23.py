def longest_digit_substring(s):
    temp = ''
    list_nums = []
    for char in s:
        if char.isdigit():
            temp += char
        else:
            if temp != '':
                list_nums.append(temp)
                temp = ''
    if temp != '':
        list_nums.append(temp)
    if len(list_nums) == 0:
        return "No digits"
    list_nums.sort(key=len)
    return list_nums[-1]

print(longest_digit_substring('sdffsd123werrer456fgdgdg1dfgdf12'))

