def find_longest_digit_substring(string):
    digit_substrings = []
    current_substring = ""

    for char in string:
        if char.isdigit():
            current_substring += char
        elif current_substring != "":
            digit_substrings.append(current_substring)
            current_substring = ""

    if current_substring != "":
        digit_substrings.append(current_substring)

    if len(digit_substrings) == 0:
        return "No digits"
    else:
        return digit_substrings[-1]

# 读取输入字符串
input_string = input()

# 调用函数查找最长数字子串并输出结果
result = find_longest_digit_substring(input_string)
print(result)

