s = input()  # 读入字符串
digits = ''  # 保存当前最长的数字子串
max_digits = ''  # 保存最终的最长数字子串

for c in s:
    if c.isdigit():  # 如果当前字符是数字
        digits += c
    else:
        if digits:  # 如果已经有数字子串
            if len(digits) >= len(max_digits): # 如果当前数字子串比最长数字子串长
                max_digits = digits  # 更新最长数字子串
            digits = ''  # 重置当前数字子串

if digits:  # 如果最后一个字符是数字，处理最长数字子串
    if len(digits) >= len(max_digits): # 如果当前数字子串比最长数字子串长
        max_digits = digits  # 更新最长数字子串

if max_digits:
    print(max_digits)  # 输出最长数字子串
else:
    print('No digits')  # 如果字符串没有数字字符，输出"No digits"
