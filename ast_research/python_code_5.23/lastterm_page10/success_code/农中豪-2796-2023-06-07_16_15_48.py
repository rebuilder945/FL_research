s = input()
digits = []
max_length = 0

# 遍历字符串中的每个字符
for c in s:
    # 如果字符是数字，则将其添加到当前数字子串中
    if c.isdigit():
        digits.append(c)
    # 如果字符不是数字，且当前数字子串不为空，则更新最长数字子串的长度和内容
    else:
        if len(digits) >= max_length:
            max_length = len(digits)
            max_digits = digits
        digits = []

# 如果字符串以数字结尾，则更新最长数字子串的长度和内容
if len(digits) >= max_length:
    max_length = len(digits)
    max_digits = digits

# 输出结果
if max_length == 0:
    print("No digits")
else:
    print("".join(max_digits))
