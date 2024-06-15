def longest_digit_substring(string):
    digits = ""
    longest_substring = ""
    string += "a"
    has_digits = False

    for char in string:
        if char.isdigit():
            digits += char
            has_digits = True
        else:
            if len(digits) >= len(longest_substring):
                longest_substring = digits
            digits = ""

    if has_digits:
        return longest_substring
    else:
        return "No digits"

# 从标准输入获取字符串
string = input()

# 获取最长数字子串并输出结果
result = longest_digit_substring(string)
print(result)

