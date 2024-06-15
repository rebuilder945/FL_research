def longest_digit_substring(string):
    digits = []
    max_length = 0
    current_length = 0

    for char in string:
        if char.isdigit():
            current_length += 1
            digits.append(char)
        else:
            if current_length > max_length:
                max_length = current_length
                digits.clear()
            current_length = 0

    if current_length > max_length:
        max_length = current_length
        digits.clear()

    if max_length == 0:
        return "No digits"
    else:
        return ''.join(digits)

# 从标准输入获取字符串
string = input()

# 获取最长数字子串并输出结果
result = longest_digit_substring(string)
print(result)

