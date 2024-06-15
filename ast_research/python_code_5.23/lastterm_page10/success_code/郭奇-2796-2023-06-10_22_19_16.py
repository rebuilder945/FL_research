s = input()  # 输入字符串
digits = ''  # 存储当前的数字子串
max_digits = ''  # 存储最长的数字子串

for i in s:
    if i.isdigit():  # 如果当前字符是数字
        digits += i  # 将其加入到当前的数字子串中
    else:  # 如果当前字符不是数字
        if len(digits) > len(max_digits):  # 更新最长的数字子串
            max_digits = digits
        digits = ''  # 清空当前的数字子串

if len(digits) > len(max_digits):  # 处理最后一个数字子串
    max_digits = digits

if max_digits == '':  # 如果没有找到任何数字子串，输出"No digits"
    print('No digits')
else:  # 输出最长的数字子串
    print(max_digits)





