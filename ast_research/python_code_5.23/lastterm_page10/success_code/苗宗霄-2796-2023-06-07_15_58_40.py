# 读入字符串
s = input()

# 初始化最长数字子串为空字符串
longest_digit_substring = ""

# 初始化当前数字子串为空字符串
current_digit_substring = ""

# 遍历字符串中的每个字符
for c in s:
    if c.isdigit():  # 如果当前字符是数字
        current_digit_substring += c  # 把当前字符加入当前数字子串
    else:  # 如果当前字符不是数字
        if len(current_digit_substring) > len(longest_digit_substring):  # 如果当前数字子串比最长数字子串更长
            longest_digit_substring = current_digit_substring  # 更新最长数字子串为当前数字子串
        current_digit_substring = ""  # 将当前数字子串重置为空字符串

# 最后需要再检查一次当前数字子串，因为程序在处理完最后一个字符之后就停止了
if len(current_digit_substring) > len(longest_digit_substring):
    longest_digit_substring = current_digit_substring

if longest_digit_substring == "":
    print("No digits")
else:
    print(longest_digit_substring)

